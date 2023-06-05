# You are given two non-empty linked lists representing two non-negative integers
# The digits are stored in reverse order, and each of their nodes contains a single digit
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # use recursion 
        # if next value exist
        #   recursion loop starts
        #   after hitting last linked list node, add current value into an array
        # then the loop goes the last linked list node and adds that value
        # so no need to sort in reverse
        arr1 = ""
        arr2 = ""
        final = 0
        def backtrack(node):
            nonlocal arr1
            if node.next != None:
                backtrack(node.next)
            arr1 = arr1 + str(node.val)

        backtrack(l1)
        final += int(arr1)
        arr1 = ""

        backtrack(l2)
        final += int(arr1)
   
        this = str(final)
        # print(str(final)[1])

        d = {}
        for x in range(len(this)):
            if x == 0:
                d[f"z{x}"] = ListNode(val=str(final)[x])
            else:
                d[f"z{x}"] = ListNode(val=str(final)[x], next=d[f"z{x-1}"])
        
        return d[f'z{len(this) - 1}']
     
        # return sum as linked list