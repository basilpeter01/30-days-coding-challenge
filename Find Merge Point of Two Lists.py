'''
day-13
Easy
Not accepted
0/7 test cases passed

'''
def findMergeNode(head1, head2):
    a = head1
    b = head2

    while a != b:
        a = a.next if a else head2
        b = b.next if b else head1
    return a.data


        