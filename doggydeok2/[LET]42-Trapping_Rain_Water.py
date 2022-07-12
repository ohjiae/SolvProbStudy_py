class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest, right_highest = [0] * len(height), [0] * len(height)
        left_highest[0], right_highest[-1] = height[0], height[-1]
        for i in range(1, len(height)):
            left_highest[i] = max(left_highest[i - 1], height[i])
            right_highest[-(i + 1)] = max(right_highest[-i], height[-(i + 1)])
        return sum([min(left_highest[i], right_highest[i]) - height[i] for i in range(len(height))])
