import sys
from collections import deque
input = sys.stdin.readline

num_of_computer = int(input())
num_of_edge = int(input())

graph = [[] for i in range(num_of_computer+1)]
check_num = [0 for i in range(num_of_computer+1)]
for i in range(num_of_edge):
    p,q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

check = deque([1])
already_visit = [1]
while check:
    now = check.popleft()
    for each in graph[now]:
        if each not in already_visit:
            check.append(each)
            already_visit.append(each)

print(len(already_visit)-1)


