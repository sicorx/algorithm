# Algorithm
# bellman-ford-moore
# node : 노드의 개수
# edge : 엣지의 개수
# arr[start, end, weight] : start->시작 노드, end->끝 노드, weight->가중치

import sys

def bfm(node, edge, arr) :
    edges = []
    weights = [sys.maxsize] * (node + 1)
    weights[1] = 0
    is_cycle = False
    
    for i in range(edge) :
        start, end, weight = map(int, arr[i])
        edges.append((start, end, weight))
    
    for _ in range(node - 1) :
        for start, end, weight in edges :
            if weights[start] != sys.maxsize and weights[end] > weights[start] + weight :
                weights[end] = weights[start] + weight
    
    for start, end, weight in edges :
            if weights[start] != sys.maxsize and weights[end] > weights[start] + weight :
                is_cycle = True
    
###################### test #################
    if not is_cycle :    #싸이클이 없는 경우
        for i in range(2, node + 1) :
            if weights[i] != sys.maxsize :
                print(weights[i])
            else :
                print(-1)
    else :  #싸이클이 있는 경우
        print(-1)


tmp = [[1, 2, 4],[1, 3, 3],[2, 3, -4],[3, 1, -2]]
tmp = [[1, 2, 4],[1, 2, 3]]

bfm(3, 2, tmp)
###################### test #################