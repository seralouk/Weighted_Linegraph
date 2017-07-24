# Weighted_Linegraph


Dependencies: numpy, igraph modules


Example:


from igraph import *

from weighted_linegraph import *

#Create a weighted graph

g = Graph()

g.add_vertices(5)

g.add_edges([(0,1),(1,2),(2,3),(3,4),(0,4)])

g.es["weight"] = range(1,g.vcount() +1)


#Call the function

weighted_lg = weighted_linegraph(g)

summary(weighted_lg)
