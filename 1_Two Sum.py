class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=0
        n=[target-i for i in nums]
        for i in range(0,len(nums)):
            a=n[i]
            n[i]=None
            if (nums[i] in n):
                return [i,n.index(nums[i])]
            n[i]=a