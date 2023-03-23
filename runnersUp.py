import heapq

n = int(input())
arr = list(map(int, input().split()))

# Find the second largest element in the list
second_largest = heapq.nlargest(2, set(arr))[-1]

print(second_largest)