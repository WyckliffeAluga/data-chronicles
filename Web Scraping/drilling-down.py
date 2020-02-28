
# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a variable with the URL to this tutorial
url = 'http://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_characters'

# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, "lxml")

# Create a variable to score the scraped data in
character_name = []

# for each item in all the toclevel-2 li items
# (except the last three because they are not character names),
for item in soup.find_all('li',{'class':'toclevel-2'})[:-3]:
    # find each span with class=toctext,
    for post in item.find_all('span',{'class':'toctext'}):
        # add the stripped string of each to character_name, one by one
        character_name.append(post.string.strip())

# View all the character names
character_name

# Create a list object where to store the for loop results
houses = []

# For each element in the character_name list,
for name in character_name:
    # split up the names by a blank space and select the last element
    # this works because it is the last name if they are a house,
    # but the first name if they only have one name,
    # Then append each last name to the houses list
    houses.append(name.split(' ')[-1])

# Convert houses into a pandas series (so we can use value_counts())
houses = pd.Series(houses)

# Count the number of times each name/house name appears
houses.value_counts()
        
