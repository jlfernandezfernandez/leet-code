from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        if flowerbed_len == 1:
            if flowerbed[0] == 0 and 0 <= n <= 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False
        for i in range(flowerbed_len):
            if n > 0:
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[0] = 1
                        n -= 1
                        continue
                if i == len(flowerbed)-1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        continue
                if (flowerbed[i] == 0):
                    if (flowerbed[i-1] == 1 or flowerbed[i+1] == 1):
                        continue
                    else:
                        flowerbed[i] = 1
                        n -= 1
        if (n == 0):
            return True
        return False
    
    def canPlaceFlowersOptimized(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        for i in range(flowerbed_len):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == flowerbed_len - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
    
def main():
    solution = Solution()
    flowerbed = [1]
    n = 0
    expected = True
    result = solution.canPlaceFlowers(flowerbed, n)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
    
if __name__ == "__main__":
    main()
