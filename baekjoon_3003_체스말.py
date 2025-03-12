horses = [1, 1, 2, 2, 2, 8]
need_horses = []

horse_input = input().split()
for i in range(0, len(horse_input)):
    horse_input[i] = int(horse_input[i])

for i in range(0, len(horses)):
    if horse_input[i] == horses[i]:
        need_horses.append(0)
    else:
        need_horses.append(horses[i] - horse_input[i])

print(*need_horses)