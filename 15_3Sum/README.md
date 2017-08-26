# 15_3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.<br>

Note: The solution set must not contain duplicate triplets.<br>

给定n个整数的数组S，S中有元素a，b，c，使得+ b + c = 0？ 查找数组中所有独特的三元组，它们的总和为零。<br>

注意：解决方案集不能包含重复的三元组。<br>

# 解题思路
三个数求其和为0，先将列表按从小到大排序，让最小的一个数i从列表的左至又遍历，然后将其余两个数设置为Left和Right;<br>

因为要求不能有重复的结果出现，所以当列表中有重复值时要将其跳过，L从i+1开始遍历，R从又往左遍历；<br>

每遍历一次求一次结果，当结果小于0时L右移一位同理当S大于0则R左移一位，当S=0时将结果添加到res中，最后遍历完将res返回即可。<br>
