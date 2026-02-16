class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uniqMinofUser  = {}
        ans = [0]*k

        for element in logs:
            user = element[0]
            time = element[1]

            if user not in uniqMinofUser:
                uniqMinofUser[user] = {time}
            else:
                uniqMinofUser[user].add(time)

        for key,value in uniqMinofUser.items():
            valu = len(value)

            if valu <= k:
                ans[valu-1] +=1
        return ans
