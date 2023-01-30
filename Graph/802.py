class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        NOT_VISITED=0
        VISITING=1
        VISITED=2
        ENTER=0
        EXIT=1
        
        def dfs(node,state):
            stack=[(node,ENTER)]
            while(stack):
                node,status=stack.pop()
                if(status==EXIT):
                    state[node]=VISITED
                else:
                    if(state[node]!=VISITED):
                        state[node]=VISITING
                        stack.append((node,EXIT))
                        for i in graph[node]:
                            if(state[i]==VISITING):
                                return
                            else:
                                if(state[i]==NOT_VISITED):
                                    stack.append((i,ENTER))

        def solve():
            state={i:NOT_VISITED for i in range(len(graph))}
            for index,value in enumerate(graph):
                if(state[index]==NOT_VISITED):
                    dfs(index,state)
            return [i for i,c in state.items() if c!=VISITING]
            # print(state)
            # return []            


        return solve()

    # Time Complexity O(n) space complexity O(n)


