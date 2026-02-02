class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = range(1,n+1)
        stack = []
        stackCapacity = len(target)
        result = []
        targetIndex = 0

        for i in stream:
            if len(stack) < stackCapacity:
                stack.append(i)
                result.append("Push")
                if targetIndex < stackCapacity:
                    if stack[-1] == target[targetIndex]:
                        targetIndex = targetIndex+1
                    else:
                        stack.pop()
                        result.append("Pop")
            else:
                if targetIndex < stackCapacity and stack[-1] != target[targetIndex]:
                    stack.pop()
                    result.append("Pop")
                    stack.append(i)
                    result.append("Push")
                else:
                    break
        return result

            
