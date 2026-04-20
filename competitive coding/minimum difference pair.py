n = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = float('inf')

for i in range(1, n):
    ans = min(ans, arr[i] - arr[i-1])

print(ans)
