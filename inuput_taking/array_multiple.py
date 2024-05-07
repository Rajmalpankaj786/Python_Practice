# input
# 2
# 5
# 1 2 3 4 5 
# 4
# 2 3 4 5

# output
# 2 3 4 5 6
# 3 4 5 6


test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(0,n):
        arr[i] += 1
    print(*arr)


