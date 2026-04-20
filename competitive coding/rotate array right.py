n, k = map(int, input().split())
arr = list(map(int, input().split()))

k = k % n  

arr = arr[-k:] + arr[:-k]

print(*arr)
