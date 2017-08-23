class Solution(object):
    def mixArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for i in range(width, -1, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L]*i), L + 1
            else:
                res, R = max(res, height[R]*i), R - 1
        return res

t = Solution()
print t.mixArea([4, 3, 7, 9, 11, 10])