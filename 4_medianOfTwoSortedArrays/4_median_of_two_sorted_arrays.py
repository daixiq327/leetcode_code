class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        len1 = len(nums3)
        if len1 % 2 == 1:
            median = nums3[(len1 - 1)/2]
        else:
            median = (nums3[len1/2] + nums3[len1/2 - 1])/2.0
        return median

t = Solution()
print t.findMedianSortedArrays([1, 3],[2])