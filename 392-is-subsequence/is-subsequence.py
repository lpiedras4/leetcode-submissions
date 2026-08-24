class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        S = len(s)
        T = len(t)
        if s == '':
            return True
        if S > T:
            return False
        
        for i in range(T):
            if s[j] == t[i]:
                j+=1
                if j == S:
                    return True
        return False