# 1 - 30 출석번호
# 28명이 제출했고 내지않은 2명 색출
# 1번째는 가장 작은 출석번호

students = [i for i in range(1, 31)]

for num in range(0, len(students) - 2):
    a = int(input())
    students.remove(a)

for i in students:
    print(i)