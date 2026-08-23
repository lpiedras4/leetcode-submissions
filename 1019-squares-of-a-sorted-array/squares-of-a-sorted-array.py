class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #O(n log n) -> Time
        # O(1) -> Space
        for i in range(len(nums)):
            num = nums[i]
            square_num = abs(num) * abs(num)
            nums[i] = square_num

        nums.sort()
        return nums