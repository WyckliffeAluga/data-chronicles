# Perform necessary imports
import pandas as pd
from bokeh.io import output_file, show , curdoc
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

df = pd.read_csv('datasets/gapminder_tidy.csv')

class Gapminder(object):
    """docstring for gapminder."""

    def __init__(self, data=None):
        if data== None:
            data = {}
        else :
            self.data = data

    def eda(self, data) :

        # Make the ColumnDataSource: source
        source = ColumnDataSource(data={
            'x'       : data.loc[1970].fertility,
            'y'       : data.loc[1970].life,
            'country' : data.loc[1970].Country,
            })

        # Create the figure: p
        p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
            plot_height=400, plot_width=700,
            tools=[HoverTool(tooltips='@country')])

            # Add a circle glyph to the figure p
        p.circle(x='x', y='y', source=source)

        # Output the file and show the figure
        output_file('gapminder.html')
        show(p)

    def beginning(self, data) :
        # Import the necessary modules
        # Make the ColumnDataSource: source
        source = ColumnDataSource(data={
            'x'       : data.loc[1970].fertility,
            'y'       : data.loc[1970].life,
            'country' : data.loc[1970].Country,
            'pop'     : (data.loc[1970].population / 20000000) + 2,
            'region'  : data.loc[1970].region,
            })

        # Save the minimum and maximum values of the fertility column: xmin, xmax
        xmin, xmax = min(data.fertility), max(data.fertility)

        # Save the minimum and maximum values of the life expectancy column: ymin, ymax
        ymin, ymax = min(data.life), max(data.life)

        # Create the figure: plot
        plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700,
            x_range=(xmin, xmax), y_range=(ymin, ymax))

        # Add circle glyphs to the plot
        plot.circle(x='x', y='y', fill_alpha=0.8, source=source)

        # Set the x-axis label
        plot.xaxis.axis_label ='Fertility (children per woman)'

        # Set the y-axis label
        plot.yaxis.axis_label = 'Life Expectancy (years)'

        # Add the plot to the current document and add a title
        curdoc().add_root(plot)
        curdoc().title = 'Gapminder'

g = Gapminder()
g.beginning(df)
