class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 2:
            return len(set(s))
        else:
            string = list(s[0])
            longest = string.copy()
            for i in range(1,  len(s)):
                if s[i] in string:
                    if len(longest) < len(string):
                        longest = string.copy()
                    string.clear()
                    for j in range(i-1, -1, -1):
                        if s[i] != s[j]:
                            string.append(s[j])
                        else:
                            string.reverse()
                            break
                string.append(s[i])
            if len(longest) < len(string):
                longest = string.copy()
        return len(longest)
