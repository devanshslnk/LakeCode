class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def createAdj():
            graph={i:set() for i in range(n)}
            neighbours={i:[] for i in range(n)}
            for conn in connections:
                graph[conn[0]].add(conn[1])
                neighbours[conn[0]].append(conn[1])
                neighbours[conn[1]].append(conn[0])
            return graph,neighbours
        def bfs():
            graph,neighbours=createAdj()
            count=0
            q=collections.deque([0])
            visited=set([0])
            while(q):
                ele=q.popleft()
                for n in neighbours[ele]:
                    if(n not in visited and ele not in graph[n]):
                        count+=1
                    if(n not in visited):
                        q.append(n)
                        visited.add(n)

            return count
        return bfs()

    # Time Complexity O(N) space Complexity O(N)

