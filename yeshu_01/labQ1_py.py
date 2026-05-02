
W, X, Y, Z = 1, 2, 3, 4

S = W + X + Y + Z
R = S
while R > 9:
    R = sum(map(int, str(R)))

x1 = R + 1
x2 = R - 1

print("R =", R)
print("Critical Points:", x1, x2)