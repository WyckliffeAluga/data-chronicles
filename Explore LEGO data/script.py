
# simple analysis of Lego Data set

# import modules
import pandas as pd

# read the colors data
colors = pd.read_csv('datasets/colors.csv')

# print the head
print(colors.head(5))

# Explore the colors
# How many number of colors are available
print((colors.shape)[0])

# Explore the distribution of transparent vs non-transparent colors
colors_summary = colors.groupby('is_trans').count()
print(colors_summary)

# Explore how the average number of parts in Lego sets have varied over years

# read the sets data
sets = pd.read_csv('datasets/sets.csv')

# create a summmary of average number of parts per year
parts_by_year = sets[['year','num_parts']].groupby('num_parts', as_index=True).mean()

# plot trends
parts_by_year.plot(x='year', y='num_parts')

# How the number of themes shipped has varied over the years
themes_by_year = sets[['year','theme_id']].groupby('year', as_index=False).agg({'theme_id': pd.Series.count})

# plot trends
themes_by_year.plot(kind='scatter', x='year', y='theme_id')

# print as sample
themes_by_year.head(5)
