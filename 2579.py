n=int(input())
score=[0]*(n+1)
cache=[[-1]*3 for _ in range(n+1)]
def maxscore(n,k):
    if n==0:
        return 0 # 계단이 0개 -> 0점 BaseCase
    if n==1:
        return score[1] # 계단이 1개 -> 1번째 계단의 점수가 최대값 -> BaseCase
    if cache[n][k]!=-1: # 0이아니다? 계산한 값이 있는거니까 그거 가져다 쓰기
        return cache[n][k]
    if k==2: # k=2면 연속으로 올라온 2번째 올라온 계단이므로 직전 계단의 최대값과 지금 계단의 값을 더하면  현재 위치에서 최대값
        cache[n][k]=maxscore(n-1,1)+score[n]
        return cache[n][k]
    if k==1: # k=1 이면 사실 직전에서 왔을 수 없지 그럼 2니까, 그렇다면 n-2에서 최대값을 구해야해 -> max n-2에서 k=2, n-2 에서 k=1 -> 그 최대값이랑 현재 계단 점수 더하면 최대값
        cache[n][k]=max(maxscore(n-2,1),maxscore(n-2,2))+score[n]
        return cache[n][k]

for i in range(1,n+1):
    score[i]=int(input())
print(max(maxscore(n, 1), maxscore(n, 2)))


