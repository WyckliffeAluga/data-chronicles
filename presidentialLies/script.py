# import some modules

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html'
r = requests.get(url)

# print some characters
#print(r.text[0:500])

# parse the html
soup = BeautifulSoup(r.text, 'html5lib')

# find all the records
records = soup.find_all('span', attrs={'class':'short-desc'})

print(len(records))
print('/n')
#print(records[0:3])
#print(records[-1])

first_record = records[0]
#print(first_record)

lieBucket = []
for record in records:
    date = record.find('strong').text[0:-1] + ', 2017'
    lie  = record.contents[1][1:-2]
    explanation = record.find('a').text[1:-1]
    url  = record.find('a')['href']
    lieBucket.append((date, lie, explanation, url))

df = pd.DataFrame(lieBucket, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('presidential_lies.csv', index=False, encoding='utf-8')
