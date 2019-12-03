n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
i = 0
while i+1 < n:
    if a[i] == a[i+1]:
        del(a[i+1])
        n -= 1
    elif a[i] != a[i+1]:
        i += 1
print(a)
