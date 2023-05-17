# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

#         s  a  c  d  b  e  t
graph = [[0, 7,10, 0, 0, 0, 0], #s
         [0, 0, 1, 8, 5, 0, 0], #a
         [0, 0, 0, 2, 0, 8, 0], #c
         [0, 0, 0, 0, 4,12, 0], #d
         [0, 0, 0, 0, 0, 9, 6], #b
         [0, 0, 0, 0, 0, 0,11], #e
         [0, 0, 0, 0, 0, 0, 0]] #t 

g = Graph(graph)

source_row = 0
target_row = 6

print("Max Flow: %d " % g.ford_fulkerson(source_row, target_row))