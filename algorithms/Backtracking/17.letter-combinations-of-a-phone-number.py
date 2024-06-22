#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, current_combination):
            if index == len(digits):
                res.append(current_combination)
                return

            for char in keys[digits[index]]:
                backtrack(index + 1, current_combination + char)

        res = []
        backtrack(0, "")
        return res


# @lc code=end
