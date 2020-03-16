"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = [starting_vertex]
        visited = set()
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current)
                visited.add(current)
                queue.extend(self.vertices[current])


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        
        stack.push((starting_vertex, self.vertices[starting_vertex]))

        while stack.size():
            vertex_id, vertex_set = stack.pop()
            print(vertex_id)
            visited.add(vertex_id)
            for vertex in vertex_set:
                if not vertex in visited:
                    visited.add(vertex)
                    stack.push((vertex, self.vertices[vertex]))

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = []
        vertices = self.vertices
        def dft_iter(starting_vertex):
            nonlocal visited
            nonlocal vertices
            print(starting_vertex)
            visited.append(starting_vertex)
            if vertices[starting_vertex]:
                for i in vertices[starting_vertex]:
                    if i not in visited:
                        visited.append(i)
                        dft_iter(i)
        dft_iter(starting_vertex=starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        queue = [[starting_vertex]]
        visited = set()
        while queue:
            path = queue.pop(0)
            if path[-1] not in visited:
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                else:
                    for neighbor in self.vertices[path[-1]]:
                        queue.append(path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()
        
        stack.push(([starting_vertex], self.vertices[starting_vertex]))

        while stack.size():
            path, vertex_set = stack.pop()
            print(path[-1])
            visited.add(path[-1])
            for vertex in vertex_set:
                if not vertex in visited:
                    visited.add(vertex)
                    stack.push((path + [vertex], self.vertices[vertex]))
                    if vertex == destination_vertex:
                        return path + [destination_vertex]

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = [starting_vertex]
        def dfs_iter(starting_vertex, destination_vertex):
            nonlocal visited
            if starting_vertex == destination_vertex:
                return [destination_vertex]
            for neighbor in self.vertices[starting_vertex]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    path = dfs_iter(neighbor, destination_vertex)
                    if path:
                        return [starting_vertex] + path
        return dfs_iter(starting_vertex, destination_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
