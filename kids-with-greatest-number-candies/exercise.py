from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for candie in candies:
            result.append(candie + extraCandies >= max_candies)
        return result
    
    
def main():
    solution = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    expected = [True,True,True,False,True]
    result = solution.kidsWithCandies(candies, extraCandies)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
    
if __name__ == "__main__":
    main()
    
        