from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
#get graph
for i in range(n):
    graph.append(list(map(int, input()[:-1])))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
apart_cnt = 0
num_of_apart = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            queue = deque([(i,j)])
            cnt = 0
            while queue:
                now = queue.pop()
                if graph[now[0]][now[1]] == 1:
                    cnt+=1
                    graph[now[0]][now[1]] = 2
                for direction in range(4):
                    next_x = now[0]+dx[direction]
                    next_y = now[1]+dy[direction]
                    if 0<=next_x<n and 0<=next_y<n:
                        if graph[next_x][next_y] == 1:
                            queue.append((next_x,next_y))
            num_of_apart.append(cnt)
            apart_cnt+=1

num_of_apart.sort()
print(apart_cnt)

for i in num_of_apart:
    print(i)

