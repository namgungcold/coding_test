a = input()
dic = {}
for i in a:
    i = i.upper()
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
max_value = max(dic.values())
max_keys = [key for key, value in dic.items() if value == max_value]
if len(max_keys)>=2:
    print("?")
else:
    print(max_keys[0])
