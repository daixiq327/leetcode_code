class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                return [dict1[nums[i]], i]
            else:
                dict1[target - nums[i]] = i

t = Solution()
print t.twoSum([3, 3], 6)
