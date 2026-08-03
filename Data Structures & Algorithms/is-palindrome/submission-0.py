class Solution:
    def isPalindrome(self, s: str) -> bool:
        concatenated_string = [c.lower() for c in s if c.isalnum()]
        return concatenated_string == concatenated_string[::-1]
