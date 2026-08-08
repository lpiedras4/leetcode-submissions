class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        res = []

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                res.append(num)
        
        for number in range(1, len(nums) + 1):
            if number not in nums:
                res.append(number)
        return res