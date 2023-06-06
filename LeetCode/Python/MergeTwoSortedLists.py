# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first check to make sure neither list is empty
        # is list is empty return other list
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        # make a starting linked list position 
        if list1.val < list2.val:
            start = ListNode(val=list1.val)
            list1 = list1.next
        else: 
            start = ListNode(val=list2.val)
            list2 = list2.next
        
        # set a pointer that will move forward, while start will stay the same to return the head of the list
        new = start
 
        # while either list is not none
        # compare values, the lesser value will become the net pointer for the new linked list
        # if list is none break loop
        while list1 is not None and list2 is not None:
            print(start, "starter")
            print(new, "new")
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
                new = new.next
            else:
                new.next = list2
                list2 = list2.next
                new = new.next
            print(list1, list2, "HEREHERHER")

        # after one of the lists equal none
        # add the rest of the other list to the next of the new linked list
        if list1 is not None:
            new.next = list1
        else:
            new.next = list2

        print(start, "BEFORE RETURN")

        return start
                

    