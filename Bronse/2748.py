a = int(input())
fib = []
for i in range(a+1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-2]+fib[i-1])

print(fib[a])