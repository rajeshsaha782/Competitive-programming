# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict

numbers = [int(n) for n in input().split()]
n = numbers[0]
m = numbers[1]

group_a = defaultdict(list)
group_b = []


for i in range(n):
    word_a = input()
    group_a[word_a].append(i+1)
    


for i in range(m):
    word_b = input()
    if word_b in group_a:
        print(' '.join(map(str,group_a[word_b])))
    else:
        print(-1)

