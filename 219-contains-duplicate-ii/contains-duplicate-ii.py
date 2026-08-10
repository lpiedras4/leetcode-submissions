class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                check_dup = abs(i - hm[nums[i]])
                if check_dup <= k:
                    return True
            hm[nums[i]] = i
        return False