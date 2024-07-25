import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
goal = (n,m)
maze = []
# get input to make maze
for line in range(goal[0]):
    maze.append(list(map(int, input()[:-1])))

graph = [[[] for j in range(m)] for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

check = deque([(0,0)])

while check:
    now_x, now_y = check.popleft()

    for i in range(4):
            next_x, next_y = now_x+dx[i], now_y+dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if maze[next_x][next_y] == 1:
                    check.append((next_x, next_y))
                    maze[next_x][next_y] = maze[now_x][now_y] + 1
        
print(maze)








# for row in range(n):
#     for col in range(m):
#         if maze[row][col] == 0:
#             continue
#         connected_node = []
#         for i in range(4):
#             next_x, next_y = row+dx[i], col+dy[i]
#             if 0<= next_x < n and 0<= next_y < m:
#                 connected_node.append((next_x, next_y))
#         graph[row][col] = connected_node

# # find shortest way
# need_visit, already_visit, check = [], [], []

# need_visit.append((0,0))

# while need_visit:
#     now = need_visit.pop(0)
#     #stop when arrive
#     if now not in already_visit:
#         already_visit.append(now)
#         if now == (n-1,m-1):
#             break
#         for each in graph[now[0]][now[1]]:
#             need_visit.append(each)
#             maze[each[0]][each[1]] = maze[now[0]][now[1]]+1

print(maze[n-1][m-1])
