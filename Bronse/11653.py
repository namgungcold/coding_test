a = int(input())
i = 2
while True:
    if a%i == 0:
        a = a//i
        print(i)
    else:
        i += 1
    if a == 1:
        break    