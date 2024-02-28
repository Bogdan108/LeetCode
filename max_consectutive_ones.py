class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        while left < len(nums):
            if nums[left] == 0:
                left += 1
            else:
                loacal_max = 0
                right = left
                while nums[right] == 1:
                    right += 1
                    loacal_max += 1
                    max_len = max(max_len, loacal_max)

        return max_len
