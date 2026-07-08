class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def dig_to_int(digit: str) -> int:
            return ord(digit) - ord('0')

        a, b = 0, 0
        for digit in num1:
            a *= 10
            a += dig_to_int(digit)
        for digit in num2:
            b *= 10
            b += dig_to_int(digit)

        result = a * b
        if result == 0:
            return "0"
        sol = ""
        
        while result > 0:
            sol += str(result % 10)
            result //= 10
        
        return sol[::-1]