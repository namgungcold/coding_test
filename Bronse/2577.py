num = 1
for i in range(3):
    num *= int(input())
num_list = [int(digit) for digit in str(num)]
cnt = [0] * 10
for i in range(len(num_list)):
    if num_list[i] == 0:
        cnt[0] = cnt[0]+1
    elif num_list[i] == 1:
        cnt[1] = cnt[1]+1
    elif num_list[i] == 2:
        cnt[2] = cnt[2]+1
    elif num_list[i] == 3:
        cnt[3] = cnt[3]+1
    elif num_list[i] == 4:
        cnt[4] = cnt[4]+1
    elif num_list[i] == 5:
        cnt[5] = cnt[5]+1
    elif num_list[i] == 6:
        cnt[6] = cnt[6]+1
    elif num_list[i] == 7:
        cnt[7] = cnt[7]+1
    elif num_list[i] == 8:
        cnt[8] = cnt[8]+1
    elif num_list[i] == 9:
        cnt[9] = cnt[9]+1
    
for i in range(len(cnt)):
    print(cnt[i])