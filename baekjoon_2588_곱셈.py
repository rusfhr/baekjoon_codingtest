# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.


a = int(input())
b = input()

list_1 = [int(i) for i in b]
list_2 = []

for i in list_1[::-1]:
    list_2.append(a * i)
    print(a * i)
    
print(a * int(b))