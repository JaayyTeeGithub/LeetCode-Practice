# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # originally tried to use a stack
        # hit some issues and don't have the debugger option
        # do i look like I have premium leetcode money?
        # so i tried something else
        # i am overcomplicating an easy problem
        # there will be much more difficult leetcode problems
        # so why bother
        
        #current_node = head
        #previous_node = None
        #stack = []
        #palindrome = False
            
        #while current_node.next is not None:
        
            #if previous_node == None:
                #stack.append(current_node)
                #previous_node = current_node
                #current_node = current_node.next
                
            #elif current_node.val != previous_node.val:
                #stack.append(current_node)
                #previous_node = current_node
                #current_node = current_node.next
                
            #elif current_node.val == previous_node.val:
                #for node in stack:
                    #stack_node = stack.pop()
                    #if stack_node == current_node:
                        #palindrome = True
                    #if stack_node != current_node:
                        #palindrome = False
                    #current_node = current_node.next
                    
        #return palindrome
        
        # lol
        val_list = []
        while head != None:
            val_list.append(head.val)
            temp = head.next
            head = temp
            
        if val_list == val_list[::-1]:
            return True
        else:
            return False