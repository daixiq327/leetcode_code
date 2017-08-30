class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        l = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(l-2):
            L, R = i + 1, l - 1
            while L < R:
                sum = nums[i] + nums[L] + nums[R]
                if abs(res - target) > abs(sum - target):
                    res = sum
                if sum == target:
                    return sum
                if sum < target:
                    L = L + 1
                if sum > target:
                    R = R - 1
        return res

t = Solution()
print t.threeSumClosest([1, 1, 0, 1], -300)

