class Solution:
    def intToRoman(self, num: int) -> str:
        roman_string = None
        integer = num
        
        if num >= 1000:
            howmany = num // 1000
            if roman_string is None:
                roman_string = 'M' * howmany
            else:
                roman_string = roman_string + 'M' * howmany
            num = num - 1000 * howmany
            
        if num >= 900:
            howmany = num // 1000
            if roman_string is None:
                roman_string = 'CM' 
            else:
                roman_string = roman_string + 'CM' 
            num = num - 900 
        
        if num >= 500:
            if roman_string is None:
                roman_string = 'D'
            else:
                roman_string = roman_string + 'D' 
            num = num - 500 
            
        if num >= 400:
            if roman_string is None:
                roman_string = 'CD'
            else:
                roman_string = roman_string + 'CD'
            num = num - 400
            
        if num >= 100:
            howmany = num // 100
            if roman_string is None:
                roman_string = 'C' * howmany
            else:
                roman_string = roman_string + 'C' * howmany
            num = num - 100 * howmany
            
        if num >= 90:
            if roman_string is None:
                roman_string = 'XC'
            else:
                roman_string = roman_string + 'XC'
            num = num - 90
            
        if num >= 50:
            if roman_string is None:
                roman_string = 'L'
            else:
                roman_string = roman_string + 'L'
            num = num - 50
            
        if num >= 40:
            if roman_string is None:
                roman_string = 'XL'
            else:
                roman_string = roman_string + 'XL'
            num = num - 40
            
        if num >= 10:
            howmany = num // 10
            if roman_string is None:
                roman_string = 'X' * howmany
            else:
                roman_string = roman_string + 'X' * howmany
            num = num - 10 * howmany
        
        if num >= 9:
            if roman_string is None:
                roman_string = 'IX'
            else:
                roman_string = roman_string + 'IX'
            num = num - 9
            
        if num >= 5:
            if roman_string is None:
                roman_string = 'V'
            else:
                roman_string = roman_string + 'V'
            num = num - 5
            
        if num >= 4:
            if roman_string is None:
                roman_string = 'IV'
            else:
                roman_string = roman_string + 'IV'
            num = num - 4
            
        if num >= 1:
            howmany = num // 1
            if roman_string is None:
                roman_string = 'I' * howmany
            else:
                roman_string = roman_string + 'I' * howmany
            num = num - 1 * howmany
            
        return roman_string
        