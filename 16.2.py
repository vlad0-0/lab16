n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
c = 1
for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            c += 1
            f = i
            s = j
    if c == 2:
        a[f] = ''
        a[s] = ''
    c = 1
i = 0
while i < len(a):
    if a[i] == '':
        del(a[i])
    else:
        i += 1
print(len(a))
print(a)
