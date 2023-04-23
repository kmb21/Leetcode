def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):

            if nums[:i+1].count(nums[i]) > 1:
                nums.pop(i)
            else:
                i+=1
        return len(nums)