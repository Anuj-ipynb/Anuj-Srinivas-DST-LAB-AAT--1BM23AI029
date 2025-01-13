def twoStacks(maxSum, a, b):
    sum_current = 0
    count = 0
    i = 0
    j = 0
    while i < len(a) and sum_current + a[i] <= maxSum:
        sum_current += a[i]
        i += 1
        count += 1

    max_count = count
    while j < len(b):
        sum_current += b[j]
        j += 1

        while sum_current > maxSum and i > 0:
            i -= 1
            sum_current -= a[i]
            count -= 1

        if sum_current <= maxSum:
            max_count = max(max_count, i + j)

    return max_count
if __name__ == "__main__":
    g = int(input().strip())  # Number of games

    for _ in range(g):
        n, m, maxSum = map(int, input().strip().split())  
        a = list(map(int, input().strip().split()))  
        b = list(map(int, input().strip().split()))  
        result = twoStacks(maxSum, a, b)
        print(result)
