class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}

        # if the lengths do not match it is false
        if len(s) != len(t):
            print(False)

        for index in range(0, len(s)):
            
            # if the key from s and value from t is not found in map add them
            if s[index] not in map:
                if t[index] not in map.values():
                    map[s[index]] = t[index]
                # if s key is found and t value is not found then it is false
                else:
                    return False
                
            # if s key is found but does not match the current index of t it is false
            elif map[s[index]] != t[index]:
                return False
            
        # if all values have been added without finding a mismatch it is true
        return True

    
