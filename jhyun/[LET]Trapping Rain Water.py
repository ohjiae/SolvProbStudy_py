class Solution:
    def trap(self, height: List[int]) -> int:
        height.insert(0, 0)
        height.append(0)
        n = len(height)
        left_h = [0] * n
        right_h = [0] * n
        max_v, answer = 0, 0
        for i in range(n):
            left_h[i] = max_v
            max_v = max(height[i], max_v)
        max_v = 0
        for i in range(n - 1, -1, -1):
            right_h[i] = max_v
            max_v = max(height[i], max_v)
        for i in range(1, n - 1):
            value = min(left_h[i], right_h[i]) - height[i]
            if value < 0:
                value = 0
            answer += value
        return answer