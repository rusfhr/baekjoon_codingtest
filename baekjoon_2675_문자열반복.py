num = int(input())

result = []

for j in range(0, num):
    a, b = input().split()
    word = ''
    
    for i in range(0, len(b)):
        word = word + (int(a) * b[i])
    
    result.append(word)

for i in range(0, len(result)):
    print(result[i])