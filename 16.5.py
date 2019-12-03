n = int(input())
a = []
j = 0
for i in range(n):
    a.append(float(input()))
    if a[-1] > 0:
        a.insert(i+j, 0)
        j += 1
print(a)
