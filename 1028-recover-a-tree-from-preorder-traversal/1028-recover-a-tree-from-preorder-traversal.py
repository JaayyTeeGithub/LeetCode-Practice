# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        head_node = TreeNode()
        depth = 0
        current_node = None
        index = 0
            
        while index in range(0, len(traversal)):
            
            if index == 0:
                index, num_string = getNumber(traversal, index)
                head_node.val = int(num_string)
            elif traversal[index] == '-':
                depth += 1
                index += 1
            else:
                current_node = head_node
                index, num_string = getNumber(traversal, index)
                    
                while depth > 0:
                    
                    # if right of current node is none go left
                    if current_node.right is not None:
                        temp_node = current_node.right
                        previous_node = current_node
                        current_node = temp_node
                        depth -= 1
                        
                    # if not go left
                    else:
                        temp_node = current_node.left
                        previous_node = current_node
                        current_node = temp_node
                        depth -= 1
  
                # once at depth if left is none make left
                if previous_node.left:
                    previous_node.right= TreeNode(int(num_string))

                # else make right
                else:
                    previous_node.left = TreeNode(int(num_string))

                        
        return head_node
    
def getNumber(traversal, index):
    num_string = ''
    while index < len(traversal) and traversal[index].isdigit():
        num_string += traversal[index]
        index += 1
    return index, num_string
                