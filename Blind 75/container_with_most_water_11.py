def maxArea(height):
    # Optimized 2 pointer approach
    # in questions like these, always think of 2 pointer approaches where you need to give an O(n) solution boiling down from O(n^2)
    # left and right ptrs, inc or dec either depending on the height at which they're in
    # if left's height is lesser than right, increment that, since we need to find a bigger height to maximize area
    # hoping to find a bigger height. 
    # So we eliminate the need to check all pairs of verticals
    left = 0
    right = len(height) - 1
    maxArea = 0
    while left < right:
        # calculate area and compare
        area = (right - left) * min(height[left], height[right])
        if height[left] <= height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        if area > maxArea:
            maxArea = area
    return maxArea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print("Max Area: ", maxArea(height))