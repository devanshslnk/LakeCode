class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 0
        GRAY = 1
        BLACK = 2
        ENTER=0
        EXIT=1
        def createGraph():
            graph={i:[] for i in range(numCourses)}
            for i in prerequisites:
                graph[i[0]].append(i[1])
            return graph
        def doDFS(graph,node,state):

            stack=[]
            stack.append((node,ENTER))
            while(stack):
                course,status=stack.pop()
                if(status==EXIT):
                    state[course]=BLACK

                else:
                    stack.append((course,EXIT))
                    state[course]=GRAY
                    for i in graph[course]:
                        if(state[i]==GRAY):
                            return True
                        if(state[i]==WHITE):
                            stack.append((i,ENTER))

            return False

        def traverse(graph):
            state=[WHITE for i  in range(numCourses)]
            for i in range(numCourses):
                if(doDFS(graph,i,state)):
                    return False

            return True


        graph=createGraph()
        return traverse(graph)


# Time Complexity O(n) SPace Complexity O(n)
