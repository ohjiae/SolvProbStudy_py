from collections import defaultdict
def solution(info, edges):
    answer = 0
    edges = defaultdict(edges)
    print(edges)
    #return answer
solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])