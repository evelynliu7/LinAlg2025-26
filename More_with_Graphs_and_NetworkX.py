# More with Graphs and NetworkX
# Some examples of generating and drawing graphs
# Patrick Honner, 10/5/2022

# Import the NetworkX package for creating graphs, matplotlib.pyplot for plotting them
import networkx as nx
import matplotlib.pyplot as plt


# Generate some built-in graphs

# Graph of the dodecahedron
G = nx.dodecahedral_graph()
# A complete graph with 6 vertices
H = nx.complete_graph(6)
# A "binomial" random graph
J = nx.gnp_random_graph(10,3)

# More graph generators here: https://networkx.org/documentation/stable/reference/generators.html


#Ploting Examples

# Create a set of drawing options for nx.draw
options = {
  'node_color': 'red',
  'node_size': 10,
  'width': 2,
}

# To just plot a single graph, uncomment the two lines of code below
#nx.draw(J, **options)
#plt.show()

# Example of putting multiple objects in a single plot

# plt.subplot creates an array of image in a single plot and specifies the location within that array

# For example, plt.subplot(231) says this plot is divided into 2 rows and 3 columns, and this particluar plot occupies the first spot
subax1 = plt.subplot(231)
nx.draw(G, **options)

# This plot occupies the third spot
subax2 = plt.subplot(233)
nx.draw(H, **options)

# This plot occupies the fifth spot
subax1 = plt.subplot(235)
# Notice that the options can be set directly in the draw call
nx.draw(J,node_color="blue",node_size=5)

# Need to tell pyplot to save the graph as an image file
plt.savefig('graph.png')
