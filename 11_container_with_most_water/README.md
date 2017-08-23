# 11_container_with_most_water
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.<br>

Note: You may not slant the container and n is at least 2.<br>

给定n个非负整数a1，a2，...，an，其中每个表示坐标（i，ai）处的点。 绘制n条垂直线，使得线i的两个端点在（i，ai）和（i，0）处。 找到两条线，它们与x轴一起形成一个容器，使得容器含有最多的水。注意：您不能倾斜容器，n至少为2。<br>

# 解题思路
本题先将两条边进行长短比较然后取较短的边，乘以宽度得到结果，然后取结果中的最大值<br>

思路是从两边往中间取值，可以将其看成是一个列表，然后分别从索引的最大和最小取值比较两值的大小，取较小的与宽度相乘并将较小的一边往前推移一位，直至遍历完取最大的值返回即可。<br>
