def twoStacks(maxSum, a, b):
    sum = 0
    count = 0
    i = 0
    j = 0
    while i < len(a) and sum + a[i] <= maxSum:
        sum += a[i]
        i += 1
        count += 1

    max_count = count
    while j < len(b):
        sum += b[j]
        j += 1

        while sum > maxSum and i > 0:
            i -= 1
            sum -= a[i]
            count -= 1

        if sum <= maxSum:
            max_count = max(max_count, i + j)

    return max_count
g = int(input().strip()) 
for _ in range(g):
    n, m, maxSum = map(int, input().strip().split())  
    a = list(map(int, input().strip().split()))  
    b = list(map(int, input().strip().split()))  
    result = twoStacks(maxSum, a, b)
    print(result)
