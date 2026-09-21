class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Approach 2 -> O(n) time and O(1) space
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count+= (1 if n == res else -1)
        return res