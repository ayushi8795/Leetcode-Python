class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashi = {}
        curr = 0
        new_str = ''

        for i in key:
            if i not in hashi and i != " ":
                x = ord('a') + curr
                if x <= ord('z'):
                    hashi[i] = ord('a') + curr
                    curr +=1
        for i in message:
            if i != " ":
                new_str = new_str + chr(hashi[i])
            else:
                new_str = new_str + " "
        return new_str