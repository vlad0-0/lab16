n = int(input())
a = []
b = []
c = 0
for i in range(n):
    a.append(int(input()))
i = 0
while len(a)>1:
    if a.count(a[i]) == 2:
        c = a[i]
        del(a[a.index(c)])
        del(a[a.index(c)])
    elif i < len(a)-1:
        i += 1
    else:
        break
print(len(a))
print(a)
