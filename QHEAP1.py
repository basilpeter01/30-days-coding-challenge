'''
Day-17
EASY
Accepted
19/19 test cases passed
'''

n=int(input())
l=[]
for i in range(n):
    val=input().split()
    a=int(val[0])
    b=int(val[1]) if len(val)>1 else 0
    if a == 1:
        l.append(b)
    if a == 2:
        l.remove(b)
    if a == 3:
        print(min(l))
