class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCount = collections.Counter(chars)
        goodS = 0

        for word in words:
            current_word = defaultdict(int)
            good = True
            for c in word:
                current_word[c] +=1
                if c not in charsCount or current_word[c] > charsCount[c]:
                    good = False
                    break
            if good:
                goodS+=len(word)
        return goodS