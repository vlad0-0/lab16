n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
    if a[-1] < 0:
        a.append(0)
print(a)
