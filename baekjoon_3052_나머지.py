i = 0

a = []

while i < 10:
    num = int(input())
    
    if num % 42 not in a:
        a.append(num % 42)

    i += 1

print(len(a))