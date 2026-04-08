class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {}
        complement = 0

        for num in range(len(nums)):
            complement = target - nums[num]

            if complement in dict:
                return [dict[complement], num]

            dict[nums[num]] = num


nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))