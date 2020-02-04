
import pickle
import matplotlib.pyplot as plt
import networkx as nx
from nxviz import MatrixPlot
from nxviz.plots import ArcPlot

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

    def matrix_plotting(self, G):
        # Calculate the largest connected component subgraph: largest_ccs
        largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]

        # Create the customized MatrixPlot object: h
        h = MatrixPlot(graph=largest_ccs)

        # Draw the MatrixPlot to the screen
        h.draw()
        plt.show()

    def arc_plotting(self, G):
        # Iterate over all the nodes in G, including the metadata
        for n, d in G.nodes(data=True):

            # Calculate the degree of each node: G.node[n]['degree']
            G.node[n]['degree'] = nx.degree(G, n)

            # Create the ArcPlot object: a
        a = ArcPlot(graph=G, node_order='degree')

        # Draw the ArcPlot to the screen
        a.draw()
        plt.show()

g = GitHub()
g.arc_plotting()
