# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))

no_cmd = int(input())

for i in range(no_cmd):
    cmd = input()
    if 'pop' in cmd:
        s.pop()
    elif 'remove' in cmd:
        c, num = cmd.split()
        s.remove(int(num))
    elif 'discard' in cmd:
        c, num = cmd.split()
        s.discard(int(num))

print(sum(s))