# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

import sys

num = int(sys.stdin.readline())
string = list(map(int, sys.stdin.readline().split()))
count = int(sys.stdin.readline())

print(string.count(count))