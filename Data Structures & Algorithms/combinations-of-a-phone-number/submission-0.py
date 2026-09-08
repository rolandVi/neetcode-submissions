class Solution:
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