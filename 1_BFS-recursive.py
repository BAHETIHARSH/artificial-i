class Graph:
    def __init__(self):
        self.graph = {"A": ['B', 'C', 'E'], "B": ['A', 'D', 'E'], "C": ['A', 'F', 'G'], "E": ['A', 'B','D'],
                      "D": ['B', 'E'],"F":[],"G":[]}

        self.queue = []
        self.visited = []
        self.bfs = []

    def BFS(self, starting_node, searching_node):
        self.queue.append(starting_node)
        while self.queue:
            val = self.queue.pop(0)
            self.visited.append(val)
            for node in self.graph[val]:
                if node not in self.visited and node not in self.queue:
                    self.queue.append(node)
            # print(self.queue)
            # print(self.visited)
            self.bfs.append(val)
            if val==searching_node:
                break
        print(self.bfs)

if __name__ == '__main__':
    G1 = Graph()
    G1.BFS("A", "F")
