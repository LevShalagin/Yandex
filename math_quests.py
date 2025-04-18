from sys import stdin
from math import gcd

while stdin:
    print(gcd(*list(map(int, input().split()))))