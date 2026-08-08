class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        res = []
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                res.append(nums[i])
        for number in range(1, len(nums) + 1):
            if number not in nums and number not in s:
                res.append(number)
        return res
