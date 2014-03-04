def eratosthenesSieve(n):
    limit = int(n ** .5)
    fin = limit + 1
    candidates = list(range(n + 1))
    for i in range(2, limit + 1):
        if candidates[i]:
            candidates[2*i::i] = [None] * len(candidates[2*i::i])
    return [i for i in candidates[2:] if i]

def modPow(a, b, m):
    if not b:
        return 1
    x = modPow(a, b/2, m)
    return (a * x ** 2) % m if b % 2 else (x ** 2) % m


start = 1
end = 4

neighbors = {}
neighbors[1] = [2,3,5]
neighbors[2] = [7, 8]
neighbors[3] = [2, 1, 5]
neighbors[5] = [1,2,3,7,8]
neighbors[8] = [4]
neighbors[4] = [1, 2]
neighbors[9] = []
neighbors[7] = []

# neighbors[node] contains all neighbors of "node"
def dfs(startNode, endNode, neighbors):
    Q, seen = [startNode], {startNode}
    while Q:
        x = Q.pop()
        print x, Q, neighbors[x]
        nbs = filter(lambda x: x not in seen, neighbors[x])
        Q.extend(nbs)
        seen.update(nbs)
        print 'after', Q, seen
    return endNode in seen


print eratosthenesSieve(100)
print modPow(2, 27, 1000), pow(2, 27, 1000)
print modPow(1723, 1941022394, 1000000), pow(1723, 1941022394, 1000000)
print modPow(-9, 7, 100), pow(-9, 7, 100)

print dfs(start, end, neighbors)
