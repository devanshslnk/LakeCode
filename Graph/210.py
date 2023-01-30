class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE=0
        GRAY=1
        BLACK=2
        ENTER=0
        EXIT=1
        def createGraph():
            graph={i:[] for i in range(numCourses)}
            for i in prerequisites:
                graph[i[0]].append(i[1])
            return graph

        def dfs(course,state,graph,finalAns):
            stack=[(course,ENTER)]
            # ans=[]
            while(stack):
                course,status=stack.pop()
                if(status==EXIT):


                    finalAns.append(course)
                    state[course]=BLACK

                else:
                    if(state[course]!=BLACK):
                        stack.append((course,EXIT))
                        state[course]=GRAY
                        for i in graph[course]:
                            if(state[i]==GRAY):
                                return False
                            elif(state[i]==WHITE):
                                stack.append((i,ENTER))

            return True
                    

        def solve():
            graph=createGraph()
            status=[WHITE for i in range(numCourses)]
            finalAns=[]
            for i in range(numCourses):
                if(status[i]==WHITE):
                    if(not dfs(i,status,graph,finalAns)):
                        return []
            return finalAns

        return solve()
                    
# Time Complexity O(n) Space Complexity O(n)
