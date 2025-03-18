# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

import sys

num = int(sys.stdin.readline())
int_list = list(map(int, sys.stdin.readline().split()))

print(min(int_list), max(int_list))