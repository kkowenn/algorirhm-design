H, T = map(int, input().split())
m = [] * T

for t in range(T):
    x = list(map(int, input().split()))
    m.append(x)

class state:
    def __init__(self, t, h):
        self.t = t
        self.h = h

def goal(s):
    if s.t == 0:
        return True
    else:
        return False

def valid(t, i):
    if i >= 0 and i < H and t >= 0:
        if m[t][i] == 0:
            return True
    return False

Q = []
for h in range(H):
    if m[T - 1][h] == 0:
        Q.append(state(T - 1, h))
        m[T - 1][h] = 2

s = Q[0]
del Q[0]
while not goal(s):
    for i in range(-1, 2):
        if valid(s.t - 1, s.h + i):
            u = state(s.t - 1, s.h + i)
            m[u.t][u.h] = 2
            Q.append(u)

    s = Q[0]
    del Q[0]

print(s.h + 1)
