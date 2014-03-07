import operator as op


s = []

y = filter(lambda x : x % 200 == 17, list(range(2000)))
z = reduce(op.mul, y, 1)
v, t = 3, 67

for u in range(10009):
    key = v * t
    z *= key

mod = (z) % 200
mod = pow(mod, 608161, 1234832)
z = 1249857123
while z > mod:
    if mod % z == 0:
        mod /= z
    z -= z & -z

s.pop()

print mod / 7
