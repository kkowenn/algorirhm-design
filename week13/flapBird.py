import copy

class State:
    def __init__(self, H, T):
        self.height = 0
        self.interval = 0
        self.H = H
        self.T = T
        self.path = []

def conflict(obstacles, state):
    if obstacles[state.interval][state.height] == 1:
        return True
    else:
        return False

def goal(state):
    return state.interval == state.T

def successors(state, obstacles):
    succ = []
    for d in [-1, 0, 1]:
        if 0 <= state.height + d < state.H:
            newState = copy.deepcopy(state)
            newState.height += d
            newState.interval += 1
            newState.path.append(newState.height)
            if not conflict(obstacles, newState):
                succ.append(newState)
    return succ

def BFS(H, T, obstacles):
    Q = [State(H, T)]
    while Q:
        s = Q.pop(0)
        if goal(s):
            return s.path
        Q.extend(successors(s, obstacles))
    return None

obstacles = []
H, T = map(int, input().split())
for _ in range(T):
    interval = list(map(int, input().split()))
    obstacles.append(interval)

path = BFS(H, T, obstacles)
print(path)
