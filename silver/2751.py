import sys
input = sys.stdin.readline
a = int(input())
num = []
for i in range(a):
    num.append(int(input()))
num.sort()
for i in num:
    print(i)