class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        decibinaries only have the value of 1 or 0
        instead of looking at this problem as a decimal summation problem
        i look at it like a summation problem of stacked binary numbers summed for a decimal solution
        each digit in the n string represents a tower and the value of the digit represents the height of the tower
        if i build the towers iteratively as a whole, i lay one brick, or 1, down for each building on each pass
        a building gets a brick if it needs one and is skipped if not, with a 0
        leading zeros distract from the solution because they are irrelevant
        the solution can be found by identifyings the largest digit in the n string
        this will effectively identify the amount of "passes" needed to build the tallest tower 
        at the end all buildings will be at their specified height
        '''
        
        # return the largest value in n:str
        largest = 0
        for char in n:
            if int(char) > largest:
                largest = int(char)
            else:
                pass
        return largest
      
            
          
            