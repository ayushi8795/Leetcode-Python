class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        pivot = len(nums)//2
        left_l = self.sortArray(nums[:pivot])
        right_l = self.sortArray(nums[pivot:])
    
        return self.merge(left_l,right_l)
    
    def merge(self, left_l,right_l):
        leftp= 0
        rightp=0
        res = []
        
        while leftp <len(left_l) and rightp <len(right_l):
            if left_l[leftp] < right_l[rightp]:
                res.append(left_l[leftp])
                leftp+=1
            else:
                res.append(right_l[rightp])
                rightp+=1
                
            
        res.extend(left_l[leftp:])
        res.extend(right_l[rightp:])
        
        return res