# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        # adjacency list
        graph = [[] for _ in range(v)]
        for u, w in edges:
            graph[u].append(w)
            graph[w].append(u)

        color = [0] * v
        def isSafe(node, col):
            for ne in graph[node]:
                if color[ne] == col:
                    return False
            return True

        def solve(node):
            if node == v:
                return True

            for col in range(1, m + 1):
                if isSafe(node, col):
                    color[node] = col

                    if solve(node + 1):
                        return True

                    color[node] = 0   # backtrack

            return False

        return solve(0)