# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add l1 values to a list
        l1_list = ['']
        l1_str = ''
        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next
        
        # reverse the list
        l1_list.reverse()
        # join the list into a string
        l1_str = ''.join(l1_list)
        # turn the string into an int
        l1_int = int(l1_str)
        
        # add l2 values to a list
        l2_list = ['']
        l2_str = ''
        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next
            
        # reverse the list
        l2_list.reverse()
        # join the list into a string
        l2_str = ''.join(l2_list)
        # turn the string into an int
        l2_int = int(l2_str)
        # find the sum of l1 int and l2 int
        total_int = l1_int + l2_int
        # turn the sum into a string
        total_str = str(total_int)
        # turn the string into a list
        total_list = list(total_str)
        # reverse the list
        total_list.reverse()

        # add indexes of the new list to a new linked list
        link_list = ListNode()
        head = link_list
        for char in total_list:
            print(char)
            head.next = ListNode(int(char))
            head = head.next
            
        # return the new linked list
        if link_list.next:
            return link_list.next
        else:
            return link_list
     
        