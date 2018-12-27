from collections import deque

class Graph:
    def __init__(self,n):
        self.edges = [[False for y in range(n)] for x in range(n)]

    def connect(self,node1,node2):
        self.edges[node1][node2] = True
        self.edges[node2][node1] = True

    def find_all_distances(self, node1):
        distances = [-1 for x in range(len(self.edges))]
        queue = deque([node1, "marker"])
        visited = set([])
        distance = 0
        while len(queue) > 1:
            nextNode = queue.popleft()
            if nextNode == "marker":
                distance = distance + 6
                queue.append("marker")
            else:
                visited.add(nextNode)
                distances[nextNode] = distance
                for num, valid in enumerate(self.edges[nextNode]):
                    if valid and num not in visited:
                        queue.append(num)
                        #test this line please
                        visited.add(num)

        distances.pop(node1)

        return distances





t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    print(' '.join(map(str,graph.find_all_distances(s-1))))


