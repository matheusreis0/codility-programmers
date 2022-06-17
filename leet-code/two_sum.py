class Solution:
    def twoSum(self, nums, target):
        for index, number in enumerate(nums):
            count = 0
            for inside_number in nums[index+1::]:
                count+=1
                if number + inside_number == target:
                    return [index, index + count]

if __name__ == '__main__':
    # print(Solution().twoSum([3,2,4], 6))
    # print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,3], 6))
