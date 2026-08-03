class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        string = s.strip()
        while (left < right):
            while left < right and not string[left].isalnum():
                left += 1
            while left < right and not string[right].isalnum():
                right -= 1

            if string[left].upper() != string[right].upper():
                return False
            left += 1
            right -= 1
        return True
