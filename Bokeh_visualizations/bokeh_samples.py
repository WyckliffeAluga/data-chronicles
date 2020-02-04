
import pandas as pd
from bokeh.plotting import figure ,ColumnDataSource
from bokeh.io import output_file , show
from bokeh.models import HoverTool

auto_df = pd.read_csv('datasets/auto-mpg.csv')
sprint_df = pd.read_csv('datasets/sprint.csv')
glucose_df = pd.read_csv('datasets/glucose.csv')

class Visualizations(object):
    """docstring for Visualizations."""

    def __init__(self, df=None):
        if df == None:
            df = {}
        else :
            self.df = df

    def auto_visualizations(self, df) :
        # use auto df
         # Create the figure: p
        p = figure(x_axis_label='HP', y_axis_label='MPG')

        # Plot mpg vs hp by color
        p.circle(df['hp'], df['mpg'], size=10, color=df['color'])
        # Specify the name of the output file and show the result
        output_file('auto-df.html')
        show(p)

    def sprint_visualization(self, df):
        # use sprint df
        # Create a ColumnDataSource from df: source
        source = ColumnDataSource(df)

        p = figure(x_axis_label='Year', y_axis_label='Time')
        # Add circle glyphs to the figure p
        p.circle(x='Year', y='Time',color='color', size=8 , source=source)

        # Specify the name of the output file and show the result
        output_file('sprint.html')
        show(p)

    def selection(self, df) :
        # use sprint df
        source = ColumnDataSource(df)
        # Create a figure with the "box_select" tool: p
        p = figure(x_axis_label='Year', y_axis_label='Time', tools='box_select')
        # Add circle glyphs to the figure p with the selected and non-selected properties
        p.circle(x='Year', y='Time', source=source,
                selection_color='red',
                nonselection_alpha=0.1)
        # Specify the name of the output file and show the result
        output_file('selection_glyph.html')
        show(p)

    def hovering(self, df):
        # use glucose_df
        source = ColumnDataSource(df)
        p = figure(x_axis_label='Time of the day', y_axis_label='Bllod glucose (mg/dL)')
        # Add circle glyphs to figure p
        p.circle(x='datetime', y='glucose', size=10, source=source,
                fill_color='grey', alpha=0.1, line_color=None,
                hover_fill_color='firebrick', hover_alpha=0.5,
                hover_line_color='white')
        # Create a HoverTool: hover
        hover = HoverTool(tooltips=None, mode='vline')

        # Add the hover tool to the figure p
        p.add_tools(hover)

        # Specify the name of the output file and show the result
        output_file('hover_glyph.html')
        show(p)

v = Visualizations()
v.hovering(glucose_df)
