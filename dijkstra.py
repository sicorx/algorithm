# dijkstra
# node : 노드 개수
# edge : 엣지 개수
# k : 출발 기준 노드
# arr[s, e, w] : s:시작 노드, e:도착 노드, w:가중치
import sys
from queue import PriorityQueue

def dijkstra(node, edge, k, arr) :
    distance = [sys.maxsize] * (node + 1)
    visited = [False] * (node + 1)
    myList = [[] for _ in range(node + 1)]
    q = PriorityQueue()

    for i in range(edge) :
        u, v, w = map(int, arr[i])
        myList[u].append((v, w))
    
    q.put((0, k))
    distance[k] = 0

    while q.qsize() > 0 :
        current = q.get()
        c_v = current[1]
        if visited[c_v] :
            continue
        visited[c_v] = True
        for tmp in myList[c_v] :
            next = tmp[0]
            value = tmp[1]
            if distance[next] > distance[c_v] + value :
                distance[next] = distance[c_v] + value
                q.put((distance[next], next))

    ################## test #################
    for i in range(1, node + 1) :
        if visited[i] :
            print(distance[i])
        else :
            print("INF")
    ################## test #################


tmp = [[5, 1, 1],[1, 2, 2],[1, 3, 3],[2, 3, 4],[2, 4, 5],[3, 4, 6]]
dijkstra(5, 6, 1, tmp)
