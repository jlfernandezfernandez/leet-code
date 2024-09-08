class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
        
        
def main():
    s = "the sky is blue"
    expected = "blue is sky the"
    result = Solution().reverseWords(s)
    print("Result:", result)
    print("Expected:", expected)
    print("Test passed:", result == expected)
    
if __name__ == "__main__":
    main()
    
    
numeros = [3, 7, 2, 9, 5, 8, 1, 6, 4, 0]

# Tareas de slicing:
# 1. Obtén los primeros 4 elementos de la lista
resultado_1 = numeros[:4]

# 2. Obtén los últimos 3 elementos de la lista
resultado_2 = numeros[-3]

# 3. Obtén los elementos del índice 2 al 7 (inclusive)
resultado_3 = numeros[2:8]

# 4. Obtén cada segundo elemento de la lista
resultado_4 = numeros[::2]

# 5. Invierte la lista
resultado_5 = numeros[::-1]

# 6. Obtén los elementos del índice 7 al 2 en orden inverso
resultado_6 = numeros[7:2:-1]

print("1:", resultado_1)
print("2:", resultado_2)
print("3:", resultado_3)
print("4:", resultado_4)
print("5:", resultado_5)
print("6:", resultado_6)