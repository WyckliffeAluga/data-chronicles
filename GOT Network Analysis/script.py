# In this project I will try to analyze the co-ocurrence network of the characters in Game of Thrones
# Two characters are considered to co-occur if their names appear in the vicinity of 15 workd from one another in the books
# The data set constitutes a network and described the edges between the characters, with some attributes attached to each edges

# Dive in

# Import modules
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# read book 1 dataset
book1 = pd.read_csv('datasets/book1.csv')

# print out a sample
print(book1.head(5))

# The data frame has 5 columns (source, target , type , weight and book )

# create an empy graph network
G_book1 = nx.Graph()

# populate the network with book1 dataframe

# iterate through the dataframe and add edges
#for _, edge in book1.iterrows():
#    G_book1.add_edge(edge['Source'], edge['Target'], weight=['weight'])

# create a list of networks for all the books
books = []
bookNames = ['datasets/book1.csv','datasets/book2.csv', 'datasets/book3.csv', 'datasets/book4.csv', 'datasets/book5.csv']

#print('hello we are done with that part')

for book_name in bookNames:
    book = pd.read_csv(book_name)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['Source'], edge['Target'], weight='weight')
    books.append(G_book)

#print('that one too sir')


# the most important character in GOT
# measure the importance of a node in a network by looking at the number of neighbours it has (the nodes it is connected to)
# this is called degree centriality

# let us extract the top 10 important characters fron book 1 and book 5

# calculate the degree centriality of book 1
deg_cen_book1 = nx.degree_centrality(books[0])

# calculate the degree of centriality of book5
deg_cen_book5 = nx.degree_centrality(books[4])

# sort the dictionaries according to their degree of centriality
sorted_deg_centriality_book1 = sorted(deg_cen_book1.items(), key=lambda x:x[1], reverse=True)[0:10]

# sort the dectionaried according to their degree of centriality
sorted_deg_centriality_book5 = sorted(deg_cen_book5.items(), key=lambda x:x[1], reverse=True)[0:10]

# print out the top 10 of book 1 and book5
#print('The top 10 of book 1 is : ', sorted_deg_centriality_book1, '/n')
#print('The top 10 of book 5 is : ', sorted_deg_centriality_book5)

# according to degree of centriality Eddard stark is the most important in book 1 but not even top 10 in book 5
# the importance of characters changes over time or just stuff happens
# lets look at that closer

# create a list of degree of centriality for all the books
evol = [nx.degree_centrality(book) for book in books]

# create a data fram from the list
degree_evol_df = pd.DataFrame.from_records(evol)

# plot the degree of centrality evolution of Eddard stark, Tyron and Jon Snoq
degree_evol_df[['Eddard-Stark', 'Tyrion-Lannister', 'Jon-Snow']].plot()
plt.show()

# What is up with Stannis ????
# Eddard starck importance dies off , snow wobbles
# We can look at various measures like betweennness centrality and pagerank

# Creating a list of betweenness centrality of all the books just like we did for degree centrality
evol = [nx.betweenness_centrality(book) for book in books]

# Making a DataFrame from the list
betweenness_evol_df = pd.DataFrame.from_records(evol)

# Finding the top 4 characters in every book
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(betweenness_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)

# Plotting the evolution of the top characters
betweenness_evol_df[list_of_char].plot(figsize=(13,7))
plt.show()
#print("woof done with that")

# we see a rise in importance of Stannis over the books although he is the third most importance according to degree centrality

# page rank was the initial way Google ranked web pages
# it evaluates the inlinks and outlinks of web pages

# let us look how the character importance according to page ranks

# create a list of page rank of all characters in all book { for value in variable}
evol = (nx.pagerank(book) for book in books)

# Making a DataFrame from the list
pagerank_evol_df = pd.DataFrame.from_records(evol)

# Finding the top 4 characters in every book
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(pagerank_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)

# Plotting the top characters
pagerank_evol_df[list_of_char].plot(figsize=(13,7))
plt.show()
