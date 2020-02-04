
import pandas as pd
from bokeh.plotting import figure ,ColumnDataSource
from bokeh.io import output_file , show

auto_df = pd.read_csv('datasets/auto-mpg.csv')
sprint_df = pd.read_csv('datasets/sprint.csv')

class Visualizations(object):
    """docstring for Visualizations."""

    def __init__(self, df=None):
        if df == None:
            df = {}
        else :
            self.df = df

    def auto_visualizations(self, df) :
         # Create the figure: p
        p = figure(x_axis_label='HP', y_axis_label='MPG')

        # Plot mpg vs hp by color
        p.circle(df['hp'], df['mpg'], size=10, color=df['color'])
        # Specify the name of the output file and show the result
        output_file('auto-df.html')
        show(p)

    def sprint_visualization(self, df):
        # Create a ColumnDataSource from df: source
        source = ColumnDataSource(df)

        p = figure(x_axis_label='Year', y_axis_label='Time')
        # Add circle glyphs to the figure p
        p.circle(x='Year', y='Time',color='color', size=8 , source=source)

        # Specify the name of the output file and show the result
        output_file('sprint.html')
        show(p)


v = Visualizations()
v.sprint_visualization(sprint_df)
