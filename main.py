import random
from graphics import *

class Graph:
    def __init__(self, vertices=25, edges_to_remove=10):
        self.vertices = vertices
        self.width = int(vertices ** 0.5)
        self.structure = {i: [] for i in range(vertices)}
        self._form_structure()
        self._remove_edges(edges_to_remove)
        
    def _form_structure(self):
        for i in range(self.vertices-1):
            if (i+1) % self.width != 0:
                self.structure[i].append(i+1)
                self.structure[i+1].append(i)
            if i < (self.vertices - self.width):
                self.structure[i].append(i+self.width)
                self.structure[i+self.width].append(i)

    def _add_edge(self, v1, v2):
        self.structure[v1].append(v2)
        self.structure[v2].append(v1)

    def _delete_edge(self, v1, v2):
        self.structure[v1].remove(v2)
        self.structure[v2].remove(v1)

    def is_connected(self):
        not_visited = [i for i in range(self.vertices)]
        queue = [0]

        while queue:
            s = queue.pop(0)
            for neighbor in self.structure[s]:
                if neighbor in not_visited:
                    not_visited.remove(neighbor)
                    queue.append(neighbor)

        return not bool(not_visited)

    def _remove_edges(self, count):
        i = 0
        while i < count:
            vertex = random.randint(0, len(self.structure)-1)
            if len(self.structure[vertex])-1 == 0:
                continue
            neighbor = random.randint(0, len(self.structure[vertex])-1)
            neighbor = self.structure[vertex][neighbor]

            self._delete_edge(vertex, neighbor)
            if not self.is_connected():
                self._add_edge(vertex, neighbor)
            else:
                i += 1
                
    def draw(self, window):
        circles = []
        for i in range(self.width):
            for t in range(self.width):
                circles.append(Point((i+1)*50,(t+1)*50))
                Circle(Point((i+1)*50,(t+1)*50), 8).draw(window)

        for i in self.structure:
            for t in self.structure[i]:
                Line(circles[i], circles[t]).draw(window)


def main():
    graph = Graph()
    win = GraphWin("graph", 500, 500)
    graph.draw(win)
    input('submit input (press "enter") to exit')
    win.close()

main()
