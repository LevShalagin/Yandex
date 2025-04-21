import sys

N = int(input())

Q = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

A, B = list(map(int, sys.stdin.readline().split()))

sum_Q = sum(Q)
sum_QC = sum(q * c for q, c in zip(Q, C))

if A == B:
    dot_product = A * sum_Q
else:
    dot_product = A * sum_Q + (B - A) * sum_QC / 255

print(int(round(dot_product)))