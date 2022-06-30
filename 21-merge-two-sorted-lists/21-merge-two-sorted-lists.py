# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # base cases
        # list1 is empty
        if not list1:
            return list2
        #list2 is empty
        elif not list2:
            return list1
        else:
            
            # if list1 is smaller
            if list1.val < list2.val:
                # recursively using next value of list1
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            # if list2 is smaller
            else:
                #recursively using next value of list2
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
                
            
        
                
        
        