from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

c = Counter(arr)

max_freq = max(c.values())

candidates = []

for key in c:
    if c[key] == max_freq:
        candidates.append(key)

print(min(candidates))
