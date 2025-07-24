class Solution:
    def isValid(self, s: str) -> bool:
        unord_map = {
            "(": ")",
            "[": "]",
            "{": "}"
            }
        if s[0] in unord_map.values() or len(s) % 2 != 0:
            return False
        brackets = []
        for i in range(len(s)):
            if s[i] in (unord_map.keys()):
                brackets.append(s[i])
            elif brackets and unord_map[brackets[-1]] == s[i]:
                brackets.pop()
            else:
                return False
        return False if brackets else True
