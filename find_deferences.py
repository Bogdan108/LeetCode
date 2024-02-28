class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first_set = set(nums1)
        seconds_set = set(nums2)
        answer = [[],[]]
        answer[0] = list(first_set - seconds_set)
        answer[1] = list(seconds_set - first_set)

        return answer
