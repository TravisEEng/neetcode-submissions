class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_alpha = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(no_alpha)-1
        while l < r:
            if no_alpha[l] != no_alpha[r]:
                return False
            r-=1
            l+=1
        return True