a = []
for i in range(10):
   a.append(int(input()))
div = [a[i]%42]
for i in range(len(a)):
    if a[i]%42 not in div:
      div.append(a[i]%42)

print(len(div))