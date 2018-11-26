#Version: Python 2.7.6
graph1 = { "1" : ["2","5"],
		  "2" : ["1","3","4"],
		  "3" : ["2","4"],
			"4" : ["2","3"],
			"5" : ["1"]
		}

graph2 =  { "1" : ["2","3"],
		  "2" : ["1"],
		  "3" : ["1"],
		}

graph3 = { "1" : ["2","3","4"],
		   "2" : ["1"],
		   "3" : ["1","2"],
		   "4" : ["1","3"]
		}


def give_simp(graph):
	i = 1
	while i < (len(graph)+1):
		n = graph[str(i)]						#n is knot whose simp is tested
		b2 = True
		j = 1	
		while j < (len(n)+1) and b2 == True:
			if j != i:
				a = graph[str(j)] 				#a are adjacent knots
				a.append(str(j))			
				if not (set(n).issubset(a)):
					b2 = False
				
				del(a[len(a)-1])
			j = j+1
		if b2 == True:
			return i							#returns the number of the knot
		i = i+1
		
print(give_simp(graph3))

s = ['1']
s.extend(str(2))
print s

def give_adj(graph,s):
	a =1
	return a
		

def create_graph(graph,n):						#creates complete graph of size n
	for i in range(0, n):
		graph.update({str(i):range(0,n)})
	return graph

#print(create_graph({},5))


def generate_edges(graph):						#returns knots and edges of graph
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

