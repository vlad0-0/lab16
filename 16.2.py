n = int(input())
a = []
c = 0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a.count(a[i]) == 2:
        c = a[i]
        del(a[a.index(a[i])])
        del(a[a.index(a[i])])
        n -= 2
print(n)
print(a)
