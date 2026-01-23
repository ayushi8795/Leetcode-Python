class Solution:
    def defangIPaddr(self, address: str) -> str:
        add = []
        for i in address:
            if i == '.':
                add.append("[.]")
            else:
                add.append(i)
        return ''.join(add)
