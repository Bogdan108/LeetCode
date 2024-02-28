class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left],  nums[right] = nums[left],  nums[right]

            if nums[left] != 0:
                left += 1
