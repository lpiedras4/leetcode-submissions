class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not s or len(s) == 1:
            return True
        lowerCaseS = s.lower()
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', lowerCaseS)

        start = 0
        end = len(cleaned_s) - 1
        while start < end:
            if cleaned_s[start] != cleaned_s[end]:
                return False
            start+=1
            end-=1
        return True
