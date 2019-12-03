n = int(input())
a = []
a.append(float(input()))
mxp = 0
mnp = 0
mxe = a[0]
mne = a[0]
for i in range(1, n):
    a.append(float(input()))
    if mxe < a[i]:
        mxe = a[i]
        mxp = i
    if mne > a[i]:
        mne = a[i]
        mnp = i
a.insert(mnp, 0)
if mnp < mxp:
    mxp += 1
a.insert(mxp+1, 0)
print(a)
