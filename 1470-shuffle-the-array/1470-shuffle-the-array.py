class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle = []
        for i in range(len(nums)-n):
            shuffle.append(nums[i])
            shuffle.append(nums[i+n])
        return shuffle