N = int(input())
cnt = 1
while cnt<=N:
    K = input()
    strick = 0
    score = 0
    for i in K:
        if i == 'O':
            strick = strick + 1 
        elif i == 'X':
            strick = 0
        score += strick 
    print(score)
    cnt = cnt + 1