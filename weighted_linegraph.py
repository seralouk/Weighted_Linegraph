from igraph import *
from numpy import *

def weighted_linegraph(g):
	"""
	Author: Serafeim Loukas, EPFL, email: serafeim.loukas(at)epfl.ch
	
	Input
	------
	g: an igraph graph object
	
	Output
	------
	lg: the weighted linegraph of the initial graph g

	"""
	g = g
	flag = g.is_connected()
	if flag:

		if len(g.es['weight']) == 0:
			lg = g.linegraph()
		else:
			es = [e.tuple for e in g.es]
			es = asarray(es)
			B = tile(0, (g.ecount(),g.vcount()))
			Btilde = tile(0, (g.ecount(),g.vcount()))
			for e in range(g.ecount()):
				B[e, es[e,]] = 1
				Btilde[e, es[e,]] = g.es['weight'][e]
			d0 = g.degree()
			d = diag(d0)
			s1 = 1.0 / asarray(d0)
			s2 = diag(s1)
			wLA = dot( dot(Btilde, s2) , Btilde.transpose() )
			A = g.get_adjacency(attribute="weight")
			A = array(A.data)
			wLA2 = dot (dot (dot (dot(Btilde,s2), A) , s2 ) , Btilde.transpose() )
			#wLA2=Btilde%*%solve(diag(degree(g)))%*%A%*%solve(diag(degree(g)))%*%t(Btilde)
			fill_diagonal(wLA2, 0)
			lg = Graph.Weighted_Adjacency(wLA2.tolist(), mode = ADJ_UNDIRECTED, attr="weight" )
	else:
		print('The graph is not connected')
		lg = None

	return lg


# Example
# Create a weighted graph

g = Graph()
g.add_vertices(5)
g.add_edges([(0,1),(1,2),(2,3),(3,4),(0,4)])
g.es["weight"] = range(1,g.vcount() +1)


# Call the function
weighted_lg = weighted_linegraph(g)
# print summary of the graph
summary(weighted_lg)
