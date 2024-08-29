from math import gcd


class Solution(object):
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
    
def main():
    solution = Solution()
    str1 = "ABCABCABC"
    str2 = "ABCABC"
    expected = "ABC"
    result = solution.gcdOfStrings(str1, str2)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
    
if __name__ == "__main__":
    main()