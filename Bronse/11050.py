a,b = map(int,input().split())
n = 1
n_k = 1
k = 1
for i in range(a,0,-1):
    n *= i
for i in range((a-b),0,-1):
    n_k *= i
for i in range(b,0,-1):
    k *= i
print(n//((n_k)*k))