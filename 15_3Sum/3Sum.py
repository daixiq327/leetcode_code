class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s < 0:
                    L = L + 1
                elif s > 0:
                    R = R - 1
                else:
                    t = [nums[i], nums[L], nums[R]]
                    res.append(t)
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
        return res

t = Solution()
print t.threeSum([-1, -1, 0, 1, 2, -4])
