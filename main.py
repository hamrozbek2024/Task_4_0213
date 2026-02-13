# 4-MASALA: Longest Increasing Subsequence (O(n log n))

import bisect

arr = [10, 9, 2, 5, 3, 7, 101, 18]
tails = []

for num in arr:
    pos = bisect.bisect_left(tails, num)
    if pos == len(tails):
        tails.append(num)
    else:
        tails[pos] = num

print(len(tails))
