from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def g(n, idk):
            if n == len(digits):
                combinations.append("".join(idk))
                return

            possible_letters = digit_to_char[digits[n]]
            for letter in possible_letters:
                idk.append(letter)
                g(n + 1, idk)
                idk.pop()

        combinations = []
        g(0, [])
        return combinations


