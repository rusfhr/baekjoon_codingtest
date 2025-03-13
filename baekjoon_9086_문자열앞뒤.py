a = int(input())

i = 0
result = []
while i < a:
    str = input()
    result.append(str[0] + str[-1])
    i += 1

for i in range(0, len(result)):
    print(result[i])