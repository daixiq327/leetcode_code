# 1_twoSum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.<br>

You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>

Example:<br>
Given nums = [2, 7, 11, 15], target = 9,<br>

Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].<br>

# 解题思路
将列表中的值依次用目标值减去，得到的结果作为键存在一个字典中，值为索引号；<br>

依次遍历当有值与字典中的键相同时取出相对应字典的值value，将之前的value和当前索引组成一个list输出。<br>
