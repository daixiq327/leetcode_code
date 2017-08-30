# 16_3Sum_Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.<br>

For example, given array S = {-1 2 1 -4}, and target = 1.<br>

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).<br>

给定n个整数的数组S，在S中找到三个整数，使得和最接近一个给定的数目target。 返回三个整数的总和。 你可以假定每个输入都只有一个解决方案.<br>

例如，给定数组S = {-1 2 1 -4}，目标= 1.<br>

最接近目标的总和为2.（-1 + 2 + 1 = 2）.<br>

# 解题思路
先将列表从小到大排序，然后求排序后的列表的前三个值的和记作res;<br>

将最小值设为i，i从列表左往右遍历，然后设置L，R分别为i+1和列表长度减1；<br>

当L<R时，设Sum为下标i,L,R的值的和，比较res和sum减去目标值的绝对值，若abs(sum-target)更小则将sum赋值为res,当sum等于目标值时直接返回，若小于目标值，则将L右移一位，同理sum大于目标值时R左移一位，遍历完全，将结果返回。<br>
