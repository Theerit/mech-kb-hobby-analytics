# Python script modified from: https://github.com/CodeSolid/python-plot-examples/blob/main/matplotlib-ipywidgets/Matplotlib_IPyWidgets_Consolidated.ipynb
# to use to update the graph
import re
import os
import json
import datetime as dt
import numpy as np
import pandas as pd

import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt

from IPython.display import display
from ipywidgets import interactive
import ipywidgets as widgets

## Figsize of 20 seems to be able to handle 1000 row of data quite well


def plot_bar_groupbuy(df_day, start_date, end_date):
	fig, ax = plt.subplots(figsize=(20, 12))
	sns.set_color_codes("pastel")

	df_update = df_day.loc[(df_day['date'] >= start_date) & (df_day['date'] <= end_date), :].copy()
	sns.barplot(x="date", y="count_product_in_day", data=df_update, hue="product", dodge=False)
	ax.tick_params(axis='x', labelrotation = 90)
	ax.grid()
	ax.set_ylabel(f'Available group buy from {start_date} to {end_date}')
	fig.tight_layout()

def do_update(df_day, start_date, end_date):
    """Based on the new control state, update the interactive plot.
    
       The approach here is to clear and redraw the whole plot rather than simply to update 
       the old one.       
    """ 
    
    plot_bar_groupbuy(df_day, start_date, end_date)
		#figure.clf()
    #configure_graph_grid()
    #line_1 = plot_line(v1, get_label("Vector 1", v1))
    #line_2 = plot_line(v2, get_label("Vector 2", v2))
    #plt.legend()
    #plt.title(get_title(v1, v2))
    #plt.draw()

def handle_event(v1_x, v1_y, v2_x, v2_y):
	"""c events from the ipywidgets.interactive handler.        
			Argument names in the event handler must match the keys in the "interactive" call (below).       
	"""

	# Repack the x and y coordinates into two vectors, and call do_update to process the change.
	vector1 = [v1_x, v1_y]
	vector2 = [v2_x, v2_y]

	do_update(vector1, vector2)


def slider_config(value):
	"""Return an IntSlider widget with the common configuration"""
	
	options = [(date.strftime(' %d %b %Y '), date) for date in dates]
	index = (0, len(options)-1)

	selection_range_slider = widgets.SelectionRangeSlider(
			options=options,
			index=index,
			description='Dates',
			orientation='horizontal',
			layout={'width': '500px'}
	)

	return selection_range_slider
	#return widgets.IntSlider(min=-6, max=6, step=1, value=value)


def init_plot(df_day):
	start_date = df_day['date'].min()
	end_date = start_date + dt.timedelta(days=100)
	plot_bar_groupbuy(df_day, start_date, end_date)

	# Make the slider controls interactive, and display them
	slider_controls = interactive(handle_event, 
									v1_x=slider_config(start_date), 
									v1_y=slider_config(vector_1[1]),
									v2_x=slider_config(vector_2[0]), 
									v2_y=slider_config(vector_2[1]))
	slider_controls.children[0].style.margin = dict(top="50px", bottom="50px", left="200px", right="50px")
	display(slider_controls)