H, T = map(int, input().split())
m = [] * T

for t in range(T):
    x = list(map(int,input().split()))
    m.append(x)

def valid(h):
    if h >= 0 and h < H:
        return True

prev_s = m[T-1][:]
for h in range(H):
    if prev_s[h] == 0:
        prev_s[h] = 'B'

t = T - 1
while t > 0:
    s = m[t-1][:]
    for h in range(H):
        for i in [-1,0,1]:
            if prev_s[h] == "B" and valid(h+i) and s[h+i] == 0:
                s[h+i] = 'B'
    prev_s = s[:]
    t -= 1

for h in range (H):
    if s[h] == 'B':
        print(h+1)
        break
