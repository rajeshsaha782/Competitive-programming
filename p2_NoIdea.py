# https://www.hackerrank.com/challenges/no-idea/problem
n, m = input().split()
arr = [int(n) for n in input().split()]
group_a = set([int(n) for n in input().split()])
group_b = set([int(n) for n in input().split()])

happiness = 0

for i in arr:
    if i in group_a:
        happiness = happiness + 1
    if i in group_b:
        happiness = happiness - 1

print(happiness)



