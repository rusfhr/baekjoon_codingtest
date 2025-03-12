dic = {'ABC' : 3,
       'DEF' : 4,
       'GHI' : 5,
       'JKL' : 6,
       'MNO' : 7,
       'PQRS' : 8,
       'TUV' : 9,
       'WXYZ' : 10}
result = 0

s = input()

for i in range(0, len(s)):
    for key in dic.keys():
        if s[i] in key:
            result += dic[key]

print(result)