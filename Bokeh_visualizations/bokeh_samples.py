
import pandas as pd
from bokeh.plotting import figure ,ColumnDataSource
from bokeh.io import output_file , show , curdoc
from bokeh.models import HoverTool, CategoricalColorMapper, Slider
from bokeh.layouts import row, widgetbox


auto_df = pd.read_csv('datasets/auto-mpg.csv')
sprint_df = pd.read_csv('datasets/sprint.csv')
glucose_df = pd.read_csv('datasets/glucose.csv')
literacy_df = pd.read_csv('datasets/literacy_birth_rate.csv')

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

    def colormapping(self, df):
        # use auto df
        # Convert df to a ColumnDataSource: source
        source = ColumnDataSource(df)

        # Make a CategoricalColorMapper object: color_mapper
        color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                       palette=['red', 'green', 'blue'])

        p = figure(x_axis_label='weight', y_axis_label='MPG')

       # Add a circle glyph to the figure p
        p.circle('weight', 'mpg', source=source,
                color=dict(field='origin', transform=color_mapper),
                legend='origin')

        # Specify the name of the output file and show the result
        output_file('colormap.html')
        show(p)

class Layouts(object):
    """docstring for Visualizations."""

    def __init__(self, df=None):
        if df == None:
            df = {}
        else :
            self.df = df

    def rows(self, df):
        # use literacy birth rate

        # Create the first figure: p1
        p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

        source = ColumnDataSource(df)

        # Add a circle glyph to p1
        p1.circle(x='fertility', y='female_literacy', source=source)

        # Create the second figure: p2
        p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

        # Add a circle glyph to p2
        p2.circle(x='population', y='female_literacy', source=source)

        # Put p1 and p2 into a horizontal row: layout
        layout = row(p1,p2)

        # Specify the name of the output_file and show the result
        output_file('fert_row.html')
        show(layout)

class app(object):
    """docstring for app."""

    def __init__(self, df=None):
        if df == None:
            df = {}
        else :
            self.df = df

    def slider(self, df) :
        # Create a slider: slider
        slider = Slider(title='my slider', start=0, end=10, step=0.1, value=2)

        # Create a widgetbox layout: layout
        layout = widgetbox(slider)

        # Add the layout to the current document
        curdoc().add_root(layout)

    def slider_data(self, x, y) :
        # Create ColumnDataSource: source
        source = ColumnDataSource({'x':x, 'y':y})

         Define a callback function: callback
            def callback(attr, old, new):

                # Read the current value of the slider: scale
                scale = slider.value

                # Compute the updated y using np.sin(scale/x): new_y
                new_y = np.sin(scale/x)

                # Update source with the new data values
                source.data = {'x': x, 'y': new_y}

                # Attach the callback to the 'value' property of slider
            slider.on_change('value', callback)

            # Create layout and add to current document

        # Add a line to the plot
        plot.line(x='x', y='y', source=source)

        # Create a column layout: layout
        layout = column(widgetbox(slider), plot)

        # Add the layout to the current document
        curdoc().add_root(layout)


v = Layouts()
v.rows(literacy_df)
