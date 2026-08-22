class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        count = collections.Counter(magazine)
        for letter in ransomNote:
            if letter not in count or count[letter]<=0:
                return False
            count[letter]-=1
        return True