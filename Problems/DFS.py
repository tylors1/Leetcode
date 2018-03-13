def creategraph(n, arr, graph):
    i = 0
    while i<2*n:
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
        i+=2

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(n, arr, graph)
        visit = [False]*(max(arr)+1)
        dfs(n, visit, graph, 1)
        print('')



