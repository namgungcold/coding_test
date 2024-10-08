N = int(input())
num = N           
count = 0         
 
while True:
    a,b=divmod(num,10)
    num=(b*10)+((a+b)%10)
    count += 1
    if(num == N):
        break
 
print(count)