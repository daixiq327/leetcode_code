# 4_Median_of_two_sorted_array
There are two sorted arrays nums1 and nums2 of size m and n respectively.<br>

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).<br>

Example 1:<br>
nums1 = [1, 3]<br>
nums2 = [2]<br>
The median is 2.0<br>

Example 2:<br>
nums1 = [1, 2]<br>
nums2 = [3, 4]<br>

The median is (2 + 3)/2 = 2.5<br>

# 解题思路
首先将两个列表合并并排序得到一个新的列表；<br>

将列表的长度模2取余，如果余数为1，则取出最中间那个数，如果余数为0，则将最中间两数相加取平均并返回结果。<br>
