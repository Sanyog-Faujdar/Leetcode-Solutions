# Problem : Container with most Water
# link : https://leetcode.com/problems/container-with-most-water/submissions/1888727753
# Approach : Greedy (move pointer with smaller height to maximize area)
# Time Complexity : O(n)
# Space Complexity : O(1)
# Insight : Area depends on min height, so move smaller pointer
#Lets start

class Solution(object):
    def maxArea(self, height):
        
        capacitys =0
        i= 0 
        j=len(height)-1
        while i<j:
            distance = j-i
            area = min(height[j],height[i]) *distance
            capacitys = max(capacitys,area)
            if height[i]>height[j]:
                j-=1
            else :
                i+=1
        return capacitys
