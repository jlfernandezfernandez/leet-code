from typing import List

class Solution:
    def productExceptSelfWrong(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            copy = nums.copy()
            copy[i] = 1
            multiply = 1
            for j in range(len(copy)):
                multiply =  multiply * copy[j]
            result.append(multiply)
        return result
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1
        for i in range(len(nums)):
            result.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
            

        
def main():
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    result = Solution().productExceptSelf(nums)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
    
if __name__ == "__main__":
    main()