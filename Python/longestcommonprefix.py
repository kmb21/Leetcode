class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        prefix = ""
        k = 1
        true = True
        for char in strs[0]:
            prefix += char
            for i in range(1, len(strs)):
                if strs[i][:k] != prefix:
                    true = False
                    break
            if not true:
                prefix = prefix[:len(prefix)-1]
                break
                
            k += 1
        return prefix