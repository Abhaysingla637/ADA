def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        # One of the two halves is always sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

def myPow(x, n):
    N = n

    # Convert negative power to its reciprocal
    if N < 0:
        x = 1 / x
        N = -N

    ans = 1

    # Binary exponentiation
    while N > 0:
        if N % 2 == 1:
            ans *= x
        x *= x
        N //= 2

    return ans

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Index of target:", search(nums, target))

x = 2.0
n = 10
print("Power:", myPow(x, n))