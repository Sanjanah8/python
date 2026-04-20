n = int(input())
arr = list(map(int, input().split()))
---------------------------------
# multiple test cases

t = int(input())
for _ in range(t):
    pass
---------------------------------
print(ans)
print(*arr)   # prints list
---------------------------------
arr = [1, 2, 3]
arr.append(4)
arr.pop()
arr.sort()
arr.sort(reverse=True)
---------------------------------
print(sum(arr))
print(max(arr))
print(min(arr))
---------------------------------
for x in arr:
    print(x)
---------------------------------
for i in range(len(arr)):
    print(arr[i])
---------------------------------
# generate all subarrays (for small n)
for i in range(n):
    for j in range(i, n):
        print(arr[i:j+1])
---------------------------------
prefix = [0]*n
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
---------------------------------
prefix[j] - prefix[i-1]
---------------------------------
s = "hello"

s[::-1]       # reverse
s.upper()
s.lower()
---------------------------------
# count chars
from collections import Counter
print(Counter(s))
---------------------------------
from collections import Counter, defaultdict, deque

Counter([1,1,2])  # {1:2, 2:1}

d = defaultdict(int)
d['a'] += 1
---------------------------------
from collections import deque

q = deque()
q.append(1)
q.popleft()
---------------------------------
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)

print(heapq.heappop(h))  # smallest
---------------------------------
heapq.heappush(h, -x)
---------------------------------
def kadane(arr):
    curr = arr[0]
    best = arr[0]

    for x in arr[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)

    return best

arr.sort()
---------------------------------
l, r = 0, n-1

while l < r:
    if condition:
        l += 1
    else:
        r -= 1
---------------------------------
l = 0
sum = 0

for r in range(n):
    sum += arr[r]

    while sum > k:
        sum -= arr[l]
        l += 1
---------------------------------
from collections import deque

q = deque([start])
visited = set([start])

while q:
    node = q.popleft()
---------------------------------
def dfs(node):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
---------------------------------
dp = [0]*n
dp[0] = arr[0]

for i in range(1,n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
---------------------------------

count = 0
---------------------------------
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
---------------------------------
arr.sort(key=lambda x: x[1])
---------------------------------
arr[::-1]
---------------------------------
curr = arr[0]
best = arr[0]

for x in arr[1:]:
    curr = max(x, curr + x)
    best = max(best, curr)

print(best)
---------------------------------
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)

print(heapq.heappop(h))  # smallest
---------------------------------
import heapq

heapq.heapify(arr)

for _ in range(k):
    x = heapq.heappop(arr)
    heapq.heappush(arr, -x)

print(sum(arr))
---------------------------------
from collections import deque

q = deque([start])
visited = set([start])
---------------------------------
def dfs(node):
    visited.add(node)
