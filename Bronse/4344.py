a = int(input())
for i in range(a):
    sum = 0
    percent_lt = []
    lt = list(map(int,input().split()))
    for j in range(len(lt)):
        if j>=1: 
            sum += lt[j]
    avg = sum/lt[0]
    for k in range(len(lt)):
        if k>=1: 
            if lt[k] > avg:
                percent_lt.append(lt[k])
    
    percentage = (len(percent_lt) / (len(lt)-1)) * 100
    print(f"{percentage:.3f}%")