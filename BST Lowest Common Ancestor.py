'''
Day-18
EASY
Accepted
10/10 test cases passed
'''


n = int(input())
values = list(map(int, input().split()))
v1, v2 = map(int, input().split())

tree = None
for val in values:
    if tree is None:
        tree = {'data': val, 'left': None, 'right': None}
    else:
        curr = tree
        while True:
            if val < curr['data']:
                if curr['left'] is None:
                    curr['left'] = {'data': val, 'left': None, 'right': None}
                    break
                curr = curr['left']
            else:
                if curr['right'] is None:
                    curr['right'] = {'data': val, 'left': None, 'right': None}
                    break
                curr = curr['right']

curr = tree
while curr:
    if v1 < curr['data'] and v2 < curr['data']:
        curr = curr['left']
    elif v1 > curr['data'] and v2 > curr['data']:
        curr = curr['right']
    else:
        break

print(curr['data'])
