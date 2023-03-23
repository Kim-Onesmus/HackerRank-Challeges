def run(n):
    sum = 0
    for i in range(1,n):
        print(i)
        sum += i
    return sum

n = int(input())
print(run(n))


# Same
n = int(input())
1 <= n <= 150
for num in range(1, n+1):
    print(num, end="")