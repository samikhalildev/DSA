
'''
    A graph is a collection of nodes, where each node can link to another node containing edges.
        - It can either directed a->b or undirected a-b. 
        - Edges can carry weights.

    When to use:
         - When you want to represent data and its relationship e.g. a social network where alex is a friend of john

    Application:
         - Find out the shortest path
         - Web crawler
         - Social network

    Terminology:
        - Strongly connected graph: A directed graph with a path from any node to any other node.
        - Strongly connected components: 
        - DAG: A graph is acyclic if there is no cycles.
        - MST: A minimum spanning tree is a subgraph that contains all vertices with no cycles (finding the minimum path that goes from one vertex to all vertices)

    Traveral: There are two common ways of searching or traversing a graph (not just graphs but relationships).
        - Deep first search: Goes deep then backtracks (using stack), time complexity O(V+E)
        - Breadth first search: Searches level by level (using queue), time complexity O(V+E)
        The steps for these algorithms are the same: Pull a vertex, process it and add it's children. The only difference is the data structure used.

    Implemention: The Graph implemention below is using HashTables to store the vertices and its edges.
        - Access, search and insertion is O(1)
        - For a directed graph, vertex deletion is O(v) where v is the number of vertices in the graph
        - For an undirected graph, deletion is O(e) where e is the number of edges from the vertex

    Methods:
        - add_vertex(vertex): Add a vertex into the graph
        - remove_vertex(vertex): Remove a vertex from the graph and all associated edges
        - contains(vertex): Check if vertex is in the graph
        - add_edge(u,v): Add an edge between 2 vertices
        - isAdjacent(u,v): Check if u is adjacent to v
        - remove_edge(u,v): Remove an edge between 2 vertices
        - get_neighbours(vertex): Get a list of edges from a vertex
        - get_graph(): Get the entire graph representation
        - get_vertices: Get all vertices in the graph
        - num_edges(): Get total edges in the graph
        - in_degree(vertex): Return the number of edges coming in to the vertex
        - out_degree(vertex): Return the number of edges leaving the vertex
        - degree(vertex): Return the degree of the vertex (both in and out edges)
        - dfs(vertex): Given a starting vertex find all vertices using deep first traversal
        - bfs(vertex): Given a starting vertex find all vertices using breadth first traversal

'''
class Graph:
    def __init__(self, graphType='undirected'):
        self.map = {}
        self.isUndirected = graphType == 'undirected' 

    def add_vertex(self, vertex):
        if vertex not in self.map:
            self.map[vertex] = {}

    def remove_vertex(self, vertex):
        if vertex not in self.map:
            return

        if self.isUndirected:
            for edge in self.map[vertex].keys():
                self.map[edge].pop(vertex)

            self.map.pop(vertex)

        else:
            for node in self.get_vertices():
                if vertex in self.map[key]:
                    self.map[key].pop(vertex)

    def add_edge(self, v, u):
        if v not in self.map:
            self.map[v] = { u: 1 }
        else:
            self.map[v][u] = 1

        if self.isUndirected:
            if u not in self.map:
                self.map[u] = { v: 1 }
            else:
                self.map[u][v] = 1

        elif u not in self.map:
            self.map[u] = {}

    def remove_edge(self, v, u):
        if v not in self.map or u not in self.map:
            return

        if u in self.map[v]:
            self.map[v].pop(u)

        if self.isUndirected and v in self.map[u]:
            self.map[u].pop(v)
    
    def isAdjacent(self, v, u):
        return v in self.map and u in self.map[v]

    def contains(self, v):
        return v in self.map

    def get_neighbours(self, vertex):
        if vertex not in self.map:
            return []

        return self.map[vertex].keys()

    def num_edges(self):
        num = 0

        for vertex in self.get_graph():
            num += len(self.map[vertex].keys())

        return num / 2 if self.isUndirected else num

    def get_graph(self):
        return self.map

    def get_vertices(self):
        return self.map.keys()

    def in_degree(self, vertex):
        num = 0

        for node in self.get_graph():
            if node is not vertex and vertex in self.map[node]:
                num += 1

        return num

    def out_degree(self, vertex):
        if vertex not in self.get_graph():
            return 0

        return len(self.map[vertex])

    def degree(self, vertex):
        return self.in_degree(vertex) + (self.out_degree(vertex) if not self.isUndirected else 0)

    def get_path(self):
        output = []

        for vertex in self.map:
            for neighbour in self.get_neighbours(vertex):
                output.append([vertex, neighbour])

        return output


    # DFS: Go deep then backtrack
    def dfs(self, v):
        output = []
        visited = set()
        stack = [v]

        while stack:
            vertex = stack.pop()
            
            # If vertex has not been visited, visit it and add it to output
            if vertex not in visited:
                visited.add(vertex)
                output.append(vertex)

                # Add all neighbours of v into the stack
                for neighbour in self.map[vertex]:
                    if neighbour not in visited:
                        stack.append(neighbour)

        return output

    # The given vertex is added to the queue and all of its children gets added to the queue level by level.
    def bfs(self, v):
        output = []
        visited = set()
        queue = [v]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.add(vertex)
                output.append(vertex)

                for neighbour in self.map[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return output

    def spanning_tree(self, v):

        spanning_tree = Graph()
        visited = set(v)
        stack = [v]

        while stack:
            vertex = stack.pop()

            # Get the first neighbour of vertex
            for neighbour in self.map[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
                    spanning_tree.add_edge(vertex, neighbour)
            
        return spanning_tree.get_path()


graph = Graph()
graph.add_vertex('a')

graph.add_edge('a','b')
graph.add_edge('a','d')
graph.add_edge('a','c')
graph.add_edge('b','c')
graph.add_edge('b','d')
graph.add_edge('c','d')

# graph.add_edge('a','b')
# graph.add_edge('a', 'f')
# graph.add_edge('f','h')
# graph.add_edge('g','f')
# graph.add_edge('b','c')
# graph.add_edge('c','e')
# graph.add_edge('d','c')

# graph.remove_edge('a', 'b')
# graph.remove_edge('g', 'f')

print(graph.get_graph())
print(graph.get_vertices())
# print(graph.get_neighbours('f'))

print(graph.num_edges())
print(graph.degree('a'))
print(graph.dfs('a'))
print(graph.bfs('a'))

print(graph.spanning_tree('a'))