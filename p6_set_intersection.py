# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
eng = set(map(int, input().split()))

m = int(input())
fre = set(map(int, input().split()))

print(len(eng.intersection(fre)))