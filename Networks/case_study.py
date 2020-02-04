
import pickle
import matplotlib.pyplot as plt
import networkx as nx

G = pickle.load(open('datasets/github_users.p', 'rb'))

class GitHub(object):
    """docstring for ."""

    def __init__(self, G=None):
        if G is None:
            G = {}
        else:
            self.G = G


    def degree_centrality_plot(self, G):
        # Plot the degree distribution of the GitHub collaboration network
        plt.hist(list(nx.degree_centrality(G).values()))
        plt.show()

    def betweenness_centrality(self, G):
        # Plot the degree distribution of the GitHub collaboration network
        plt.hist(list(nx.betweenness_centrality(G).values()))
        plt.show()

g = GitHub()
g.betweenness_centrality(G)
