class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current_max = None

        for num in nums:
            if count==0:
                current_max = num
            count += (1 if num == current_max else -1)
        return current_max