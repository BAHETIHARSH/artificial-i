class Graph:
    def __init__(self):
        self.graph = {"A": ['B', 'C', 'E'],
                      "B": ['A', 'D', 'E'],
                      "C": ['A', 'F', 'G'],
                      "E": ['A', 'B','D'],
                      "D": ['B', 'E'],
                      "F":[],
                      "G":[]}

        self.queue = []
        self.bfsvisited = []
        self.bfs = []
        self.dfs = []
        self.dfsvisited = []
        self.stack = []

    def BFS(self,start,goal):
        self.queue.append(start)
        while(self.queue):
            val = self.queue.pop(0)
            self.bfsvisited.append(val)
            if val == goal:
                break
            for i in self.graph[val]:
                if i not in self.bfsvisited and i not in self.queue:
                    self.queue.append(i)
        print("BFS SEARCH PATH",self.bfsvisited)


    def DFS(self,start,goal):
        self.stack.append(start)
        while self.stack :
            val = self.stack.pop()
            self.dfsvisited.append(val)
            if val== goal:
                break
            for i in self.graph[val]:
                if (i not in self.dfsvisited) and (i not in self.stack):
                    self.stack.append(i)

        print("DFS SEARCH PATH :",self.dfsvisited)
if __name__ == '__main__':
    G1 = Graph()
    G1.DFS("A", "G")
    G1.BFS("A", "G")

