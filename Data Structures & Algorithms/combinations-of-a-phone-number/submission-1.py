class Mine:
    def letterCombinations(self, digits: str) -> List[str]:
        mapa: Dict[str, Set[str]] = {
            "2": {"a", "b", "c"},
            "3": {"d", "e", "f"},
            "4": {"g", "h", "i"},
            "5": {"j", "k", "l"},
            "6": {"m", "n", "o"},
            "7": {"p", "q", "r", "s"},
            "8": {"t", "u", "v"},
            "9": {"w", "x", "y", "z"}
        }

        if not digits:
            return []

        sol = [""]
        for dig in digits:
            temp_array = []
            for char in mapa.get(dig):
                for entry in sol:
                    temp_array.append(entry + char)
            sol = temp_array.copy()

        return sol

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res