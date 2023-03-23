<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- Probably does not need the shield just yet 

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO # No logo as of now as well
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

-->

<!-- TABLE OF CONTENTS 
let's stash this for now

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
-->


<!-- ABOUT THE PROJECT -->
## About The Project

![Cover Photo][cover-photo]

Hi, welcome to my side project repository. This project is a sort of passion work of mine and it also serves to answer some of my curiousity regarding the statistics of mechanical keyboard group buy world. In this project, so far, I have done the followings
* Scrape the group buy data from subreddit https://www.reddit.com/r/MechGroupBuys/
* Extract the information, e.g. price, start date, vendor information of each group buy. (Lots of assumptions were made)
* Parse the information into the dataframe
* Visualize the dataframe to understand the data more, e.g. distribution of each group buy products, majority keycap vendors, how many group buys are available during the past 3 years.


<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



### Built With

<!-- * [![Next][Next.js]][Next-url] Keep this as an example -->
* [pandas][pandas-url]
* [numpy][numpy-url]
* [jupyter][jupyter-url]
* [seaborn][seaborn-url]
* [ipywidget][ipywidget-url]
* [praw][praw-url]
* [pushshift][pushshift-url]

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- GETTING STARTED -->

<!-- will shelf the getting started, prerequisites, installation for now, maybe change to some of the assumptions/analysis instead? 
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->

<!-- USAGE EXAMPLES -->
## Mech KB Group Buy Analysis

I have attached the video screen shot of some of the analysis I have done. It shows the amount of the available group buy of each mechanical keyboard product types (keyboard, keycap, deskmat, and switches) with the group buy start date of March-2020.

* We can see that keycap dominates the group buy market in terms of number
* Mechanical keyboard, even though has lower product counts, can compete with the keycaps in terms of the prices
* We can see that the number of group buy peaks around 2021, and drops down from there (perhaps correlates with other world events)

Please visit EDA.ipynb or EDA.pdf for more analysis.

![Stack Plot Count Video][stack-plot-count-video]

![Stack Plot Price Video][stack-plot-price-video]

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
## Roadmap

- [ ] Properly add the markdown to the notebook
- [ ] Change the font of the screen shot (images and videos)
- [ ] Find ways to extract the shipping date from current data
- [ ] Include plot that involves the vendor information (distribution or etc.)
- [ ] Think of ways to differentiate keyboard types (tkl, 65, 75, etc.)
- [ ] Find a way to circumvent Reddit API limit of 1000 (pushshift hasn't worked for me so far)
- [ ] Correlate group buy stack plot with possible world event (covid?)

<!-- probably don't need this line right now
See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues). -->

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
## Contributing

Feel free to open the issues if you have any comments or questions. Criticisms are also welcome. Feel free to fork the repo and create pull request if you would like to colloborate as well.

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Your Name - theerit.l@gmail.com

Project Link: [https://github.com/Theerit/mech-kb-hobby-analytics](https://github.com/Theerit/mech-kb-hobby-analytics)

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
I would like to acknowledge the following repository as I borrow/copy codes from them
* [reddit_scraping](https://github.com/parth647/reddit_scraping_using_praw/)
* [Reddit_Image_Scraper](https://github.com/D3vd/Reddit_Image_Scraper)
* [python-plot-examples](https://github.com/CodeSolid/python-plot-examples)
* [Best-README-Template] (https://github.com/othneildrew/Best-README-Template)

<!-- stash this for now <p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[cover-photo]: images/cover_photo.png
[stack-plot-count-video]: image/stack_plot_count_record.mov
[stack-plot-price-video]: image/stack_plot_price_record.mov
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[pandas-url]: https://pandas.pydata.org/
[numpy-url]: https://numpy.org/
[matplotlib-url]: https://matplotlib.org/
[jupyter-url]: https://jupyter.org/
[seaborn-url]: https://seaborn.pydata.org/
[ipywidget-url]:https://ipywidgets.readthedocs.io/en/stable/
[praw-url]: https://praw.readthedocs.io/en/stable/
[pushshift-url]: https://github.com/pushshift/api