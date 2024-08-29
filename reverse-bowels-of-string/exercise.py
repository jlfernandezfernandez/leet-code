class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        string_list = list(s)
        string_length = len(string_list)
        string_vowels = []
        i = 0
        while i < string_length:
            if s[i].lower() in vowels:
                string_vowels.append(string_list[i])
            i += 1
        i = 0
        while i < string_length:
            if s[i].lower() in vowels:
                string_list[i] = string_vowels.pop()
            i += 1
        return "".join(string_list)
    
    def reverseVowelsOptimized(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
       
def main():
    s = "hello"
    expected = "holle"
    result = Solution().reverseVowels(s)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
        
if __name__ == "__main__":
    main()