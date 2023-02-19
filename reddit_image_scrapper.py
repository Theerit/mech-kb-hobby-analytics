import re, os, time
import praw
import configparser
import urllib.request

from prawcore.exceptions import Redirect
from prawcore.exceptions import ResponseException
from urllib.error import HTTPError


class ClientInfo:
  id = ''
  secret = ''
  user_agent = 'Reddit_Image_Scraper'


def get_client_info():
  config = configparser.ConfigParser()
  config.read("config.ini")
  id = config["ALPHA"]["client_id"]
  secret = config["ALPHA"]["client_secret"]

  return id, secret


def save_list(img_url_list):
  for img_url in img_url_list:
    file = open('img_links.txt', 'a')
    file.write('{} \n'.format(img_url))
    file.close()


def delete_img_list():
  f = open('img_links.txt', 'r+')
  f.truncate()


def is_img_link(img_link):
  ext = img_link[-4:]
  if ext == '.jpg' or ext == '.png':
    return True
  else:
    return False


def get_img_urls(submission):
  try:
    #r = praw.Reddit(client_id=ClientInfo.id, client_secret=ClientInfo.secret, user_agent=ClientInfo.user_agent)
    #submissions = r.subreddit(sub).hot(limit=li)
    
    # Possible work around to get the the image url from the reddit
    #gallery_url  = 'https://www.reddit.com/r/announcements/comments/hrrh23/now_you_can_make_posts_with_multiple_images/'
    #submission = reddit.submission(url = gallery_url)
    
    image_url_list = []
    #for submission in submissions:
    image_dict = submission.media_metadata
    for image_item in image_dict.values():
      largest_image = image_item['s']
      image_url = largest_image['u']
      image_url_list.append(image_url)
    
    #return [submission.url for submission in submissions]
    return image_url_list

  except Redirect:
    print("Invalid Subreddit!")
    return 0

  except HTTPError:
    print("Too many Requests. Try again later!")
    return 0

  except ResponseException:
    print("Client info is wrong. Check again.")
    return 0


def download_img(img_url, img_title, filename):
  opener = urllib.request.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/5.0')]
  urllib.request.install_opener(opener)
  try:
    print('Downloading ' + img_title + '....')
    urllib.request.urlretrieve(img_url, filename)
    return 1

  except HTTPError:
    print("Too many Requests. Try again later!")
    return 0


def read_img_links(sleep_interval):
  with open('img_links.txt') as f:
    links = f.readlines()

  links = [x.strip() for x in links]
  download_count = 0

  for link in links:
    
    # Add sleep the code to avoid overwhelming the reddit PRAW API
    time.sleep(sleep_interval)
    
    #if not is_img_link(link):
    #  continue
    # With new code that get reddit submission metadata, checking for img_link might not be needed

    #file_name = link.split('/')[-1]
    
    # Current format of the files is: qqij9wiyneia1.png?width=3000&format=png&auto=webp&v=enabled&s=97450fe5838e641497b01e0222f5593d043b24b4
    # Use regex to get the the proper filename.    
    file_name = re.search("(\w*\.png|\.jpg|\.jpeg)\d*", link.lower()).group(1)
    os.makedirs('result', exist_ok=True)
    file_loc = 'result/{}'.format(file_name)

    if not file_name:
      continue

    download_status = download_img(link, file_name, file_loc)
    download_count += 1

    if download_status == 0:
      return download_count, 0

  return download_count, 1


#if __name__ == '__main__':

def get_img_subreddit(submission, num_img_limit=100, sleep_interval=3):
  """Pass in list of PRAW reddit submission"""

    
  # Change from list of submission to allow for integration between text mining module and image one
  url_list = get_img_urls(submission)
  file_no = 1

  if url_list:

    save_list(url_list)
    count, status = read_img_links(sleep_interval)

    if status == 1:
        print('\nDownload Complete\n{} - Images Downloaded\n{} - Posts Ignored'.format(count, num_img_limit - count))
    elif status == 0:
        print('\nDownload Incomplete\n{} - Images Downloaded'.format(count))

  delete_img_list()