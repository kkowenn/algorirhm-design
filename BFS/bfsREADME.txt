marked = [False] * G.size()
def bfs (G, v) :
    queue = [U]
    while len (queue) > 0:
        0 = queue.pop(0)
        if not marked u:
            visit (v)
            marked [v] = True
            for w in G.neighbors(v):
                if not marked[w]:
                    queue.append(w)
