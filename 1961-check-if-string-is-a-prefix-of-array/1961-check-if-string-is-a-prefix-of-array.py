class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        newlis = []

        if len(words) == 1 and s == words[0]:
            return True
        else:
            slow = 0
            fast = slow+1
            while slow < fast and fast < len(words)+1 :
                neword = "".join(words[slow:fast])
                if neword == s: # if s formed no need to add all possible to list
                    return True
                if len(neword) < len(s): # if length increases more than s no need just return false
                    fast = fast + 1
                else:
                    return False
        return False

        