class Solution:

    def minTimeToType(self, word: str) -> int:
        time = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        start = 0
        end = 26
        
        for index in range(0, len(word) - 1):
            current_pos = alphabet.find(word[index])
            next_pos = alphabet.find(word[index + 1])
            a_pos = 0
            
            if index == 0 and word[index] == 'a':
                time += 1
            elif index == 0 and word[index] != 'a':
                path_a = len(alphabet[a_pos:current_pos])
                path_b = len(alphabet[current_pos:end])
                if path_a <= path_b:
                    time += path_a + 1
                else:
                    time += path_b + 1

            if current_pos == next_pos:
                time += 1

            elif current_pos < next_pos:
                path_a = len(alphabet[current_pos:next_pos])
                path_b = len(alphabet[start:current_pos]) + len(alphabet[next_pos:end])

                if path_a <= path_b:
                    time += path_a + 1
                else:
                    time += path_b + 1

            elif current_pos > next_pos:
                path_a = len(alphabet[next_pos:current_pos])
                path_b = len(alphabet[start:next_pos]) + len(alphabet[current_pos:end])

                if path_a <= path_b:
                    time += path_a + 1
                else:
                    time += path_b + 1
           

        return time
        