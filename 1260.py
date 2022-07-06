from collections import deque

n,m,v = map(int,input().split())
arr = [[]*1000 for _ in range(1001)]
bool = [False]*1001
bool2 = [False]*1001


def dfs(n):

    bool[n]=True
    print(n,end=" ")
    for next in arr[n]:
        if bool[next] == False:
            dfs(next)
for i in range(0,m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1,n+1):
    arr[i].sort()

dfs(v)
print()

deq=deque()
deq.appendleft(v)
while(deq):
    tmp=deq.pop()
    if(bool2[tmp]==True):
        continue
    bool2[tmp]=True
    print(tmp,end=" ")
    for i in arr[tmp]:
        deq.appendleft(i)


