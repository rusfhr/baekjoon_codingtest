word = input()

string = 'abcdefghijklmnopqrstuvwxyz'

result = []

for i in string:
    if i in word:
        result.append(word.index(i))

    else:
        result.append(-1)

print(*result)