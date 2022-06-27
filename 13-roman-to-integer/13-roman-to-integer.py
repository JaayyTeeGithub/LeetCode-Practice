class Solution:
    def romanToInt(self, s: str) -> int:
        previous_numeral = None
        roman_string = s
        total = 0
        for index in range(0, len(roman_string)):
            
            if roman_string[index] == 'I':
                total += 1
                
            elif roman_string[index] == 'V':
                if previous_numeral == 'I':
                    total += 3
                else:
                    total += 5
                
            elif roman_string[index] == 'X':
                if previous_numeral == 'I':
                    total += 8
                else:
                    total += 10
                
            elif roman_string[index] == 'L':
                if previous_numeral == 'X':
                    total += 30
                else:
                    total += 50
                
            elif roman_string[index] == 'C':
                if previous_numeral == 'X':
                    total += 80
                else:
                    total += 100
                
            elif roman_string[index] == 'D':
                if previous_numeral == 'C':
                    total += 300
                else: 
                    total += 500
                   
            elif roman_string[index] == 'M':
                if previous_numeral == 'C':
                    total += 800
                else:
                    total += 1000
                  
            previous_numeral = roman_string[index]
                    
        return total
        
                
            
                