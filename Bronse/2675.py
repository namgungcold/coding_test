a = int(input())
str_1 = 'lt'
for i in range(a):
    num,str_1 = input().split()
    num = int(num)
    for s in str_1:
        print(s*num,end='')
    print()