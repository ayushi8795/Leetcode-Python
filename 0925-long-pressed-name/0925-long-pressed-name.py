class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False

        namepointer = typedpointer = 0

        while namepointer < len(name) and typedpointer < len(typed):
            if name[namepointer] == typed[typedpointer]:
                namepointer +=1
                typedpointer+=1
            elif typedpointer >=1 and typed[typedpointer] == typed[typedpointer-1]:  # check if the vurrent typed char is long pressed of prev char
                typedpointer+=1
            else:
                return False

        if namepointer != len(name):
            return False
       
        # check if previos element is same the the current one [especially for the last element when last char can be typed more than once]
        while typedpointer < len(typed):
            if typed[typedpointer] != typed[typedpointer-1]:
                return False
            typedpointer+=1
        
        return True
        

        

        