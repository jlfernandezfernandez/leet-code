class Solution(object):
    def mergeAlternately(self, word1: str, word2: str):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i = 0
        while i < word1.__len__() and i < word2.__len__():
            result = result + word1[i]
            result = result + word2[i]
            i = i + 1
        result = result + word1[i:]
        result = result + word2[i:]
        return result

    ## Better solution:
    def mergeAlternatelyOptimized(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) and i < len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        result.append(word1[i:])
        result.append(word2[i:])
        return "".join(result)


def main():
    solution = Solution()
    word1 = "abcaab"
    word2 = "defz"
    expected = "adbecfazab"
    result = solution.mergeAlternately(word1, word2)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)


if __name__ == "__main__":
    main()
