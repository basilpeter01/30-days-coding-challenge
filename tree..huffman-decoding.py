'''
day-11
MEDIUM
Not accepted
0/7 test cases passed
'''

def decodeHuff(root, s):
    curr = root
    for bit in s:
        if bit == '0':
            curr = curr.left
        else:
            curr = curr.right

        if curr.left is None and curr.right is None:
            print(curr.data, end='')
            curr = root
root =input()
s=input()
decodeHuff(root,s)