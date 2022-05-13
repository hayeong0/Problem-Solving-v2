# 42. Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]):
        if len(height) == 0:
            return 0

        water = 0
        start, end = 0, len(height)-1   
        start_max, end_max = height[start], height[end] 

        while start < end: 
            start_max, end_max = max(start_max, height[start]), max(end_max, height[end])

            if start_max <= end_max: 
                water += start_max-height[start]
                start += 1
            else:
                water += end_max-height[end]
                end -= 1

        return water

if __name__ == '__main__':
    test_case = [4,2,0,3,2,5]
    print(Solution().trap(test_case))