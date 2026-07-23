class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l < r:
            l_letter = s[l]
            r_letter = s[r]
           # temp_l = l_letter
           # temp_r = r_letter
            s[r] = l_letter
            s[l] = r_letter
            r-=1
            l+=1