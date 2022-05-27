a = '7641'
b = '7621'

c = 1 << 7
c = c | 1 << 6
c = c | 1 << 4
c = c | 1 << 1

d = 1 << 7
d = d | 1 << 6
d = d | 1 << 2
d = d | 1 << 1
f = c ^ d
print(bin(d))
print(bin(c))

print(bin(c ^ d))
print((c ^ d))
cnt = 0
for i in range(1, 7) :
    comp = 1 << i
    if (f & comp) > 0 :
        cnt += 1
print(cnt)