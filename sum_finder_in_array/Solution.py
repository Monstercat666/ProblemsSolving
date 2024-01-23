
class Solution:
    def __init__(self, nums, target):
        def findSum(nums, target):
            sumMemory = {}
            for num in nums:
                remaining = target - num
                if remaining in sumMemory:
                    return True
                else:
                    sumMemory[num] = remaining
            return False

        print(findSum(nums, target))

Solution([10, 12, 3, 3, 17, 1], 17)

