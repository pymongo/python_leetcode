class Solution:
    def fizzBuzz(self, n):
        result = []
        for num in range(1, n + 1):
            if num % 3 == 0:
                if num % 5 == 0:
                    result.append("fizz buzz")
                else:
                    result.append("fizz")
            elif num % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(num))
        return result
