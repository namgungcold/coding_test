
N = int(input())
a = list(map(int,input().split()))
max = 0
for i in a:
    if max <i:
        max = i
sum = 0
for i in a:
    sum += i/max*100
print(sum/N)