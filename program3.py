from typing import List, Tuple

# Find Kth Largest Element
def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


# Find Minimum and Maximum
def findMinMax(nums: List[int]) -> Tuple[int, int]:
    minimum = maximum = nums[0]

    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum


# Main Program

nums = [3, 2, 1, 5, 6, 4]

k = 2

print("Kth Largest Element:", findKthLargest(nums, k))

print("Minimum and Maximum:", findMinMax(nums))
