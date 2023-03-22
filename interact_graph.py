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
from matplotlib.ticker import MaxNLocator

from IPython.display import display
from ipywidgets import interactive
import ipywidgets as widgets

## Figsize of 20 seems to be able to handle 1000 row of data quite well


def plot_bar_groupbuy(df_widget, start_date, end_date):			

	plt.close()

	fig_widget, ax_widget = plt.subplots(figsize=(10, 6))
	#fig_widget = plt.figure(figsize=(20, 12))
	
	df_update = df_widget.loc[(df_widget['date'] >= start_date) & (df_widget['date'] <= end_date), :]
	ax_widget.yaxis.set_major_locator(MaxNLocator(integer=True))
	ax_widget.xaxis.set_major_locator(MaxNLocator(integer=True))
	prod_col = [col for col in df_update.columns if col.startswith('count')]
	stack_list = []
	for col in prod_col:
		stack_list.append(df_update[col])
	stack_plot = np.vstack(stack_list)
	ax_widget.stackplot(df_update['str_date'], stack_plot, 
		     labels=[col.replace('count_', '').replace('_in_day', '') for col in df_update.columns if col.startswith('count')])
	
	ax_widget.legend()
	ax_widget.grid()
	ax_widget.tick_params(axis='x', labelrotation = 90)
	ax_widget.set_title(f'Available group buy from {start_date.strftime("%d-%b-%Y")} to {end_date.strftime("%d-%b-%Y")}')
	fig_widget.tight_layout()		
	

def do_update(df_widget, start_date, end_date):
    """Based on the new control state, update the interactive plot.
    
       The approach here is to clear and redraw the whole plot rather than simply to update 
       the old one.       
    """ 
    
    plot_bar_groupbuy(df_widget, start_date, end_date)
		#figure.clf()
    #configure_graph_grid()
    #line_1 = plot_line(v1, get_label("Vector 1", v1))
    #line_2 = plot_line(v2, get_label("Vector 2", v2))
    #plt.legend()
    #plt.title(get_title(v1, v2))
    #plt.draw()

def handle_event(date_range):
	"""c events from the ipywidgets.interactive handler.        
			Argument names in the event handler must match the keys in the "interactive" call (below).       
	"""

	start_date = date_range[0]
	end_date = date_range[1]

	do_update(df_widget, start_date, end_date)


def date_slider_config(start_date, end_date, end_date_max):
	"""Return an IntSlider widget with the common configuration"""
	
	dates = [start_date + dt.timedelta(days=x) for x in range((end_date_max - start_date).days)]
	options = [(date.strftime(' %d %b %Y '), date) for date in dates]
	index = (0, len(options)-1)

	selection_range_slider = widgets.SelectionRangeSlider(
			value = (start_date, end_date),
			options=options,
			index=index,
			description='Dates',
			orientation='horizontal',
			layout={'width': '800px'},
			continuous_update=False
	)

	return selection_range_slider
	#return widgets.IntSlider(min=-6, max=6, step=1, value=value)


def init_plot(df_day):

	global df_widget
	df_widget = df_day.copy()	
	df_widget['str_date'] = df_widget['date'].dt.date.astype(str)	
	start_date = df_widget['date'].min()
	end_date = start_date + dt.timedelta(days=150)
	end_date_max =  df_widget['date'].max()
	#plot_bar_groupbuy(df_widget, start_date, end_date)

	# Make the slider controls interactive, and display them
	slider_controls = interactive(handle_event,
									date_range=date_slider_config(start_date, end_date, end_date_max)
									)									
	#slider_controls.children[0].style.margin = dict(top="50px", bottom="50px", left="200px", right="50px")
	display(slider_controls)