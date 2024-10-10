a,b = map(int,input().split())
day = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mon_31 = [1,3,5,7,8,10,12]
mon_30 = [4,6,9,11]
num = 0
if a > 1:
    for i in range(1,a):
        if i in mon_31:
            num += 31
        elif i in mon_30:
            num += 30
        else:
            num += 28
    num += b
else:
    num += b

print(day[num%7])