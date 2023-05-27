
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index1 in range(len(nums)-1):
        for index2 in range(index1+1, len(nums)):
            if nums[index1] + nums[index2] == target:
                return [index1, index2]
lst = ["hi","helo","bye"]
z = enumerate(lst)
for i,j in z:
    print(i,j) 