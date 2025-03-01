# 과목수 n 개
# 자기 점수 최대값 m 
# 모든 점수 / m * 100 으로 고친다

n = int(input())

num = 0
score_list = input().split()

for i in range(0, n):
    score_list[i] = int(score_list[i])

score_list.sort()

m = max(score_list)

for i in range(0, n):
    score_list[i] = score_list[i] / m * 100

print(sum(score_list) / n)