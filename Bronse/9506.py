while True:
    a = int(input())
    if a == -1:
        break
    lt = []
    sum = 0
    for i in range(1,a):
        if a%i == 0:
            lt.append(i)
            sum += i
    if a == sum:
        print(f"{a} = ",end='')
        for i in range(len(lt)):
            print(f"{lt[i]}",end='')
            if (i+1) == len(lt):
                break
            print(f" + ",end='')
        print()
    else:
        print(f"{a} is NOT perfect.")
    