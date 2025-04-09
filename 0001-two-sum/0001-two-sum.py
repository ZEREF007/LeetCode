class Solution:
    def twoSum(self, num, target):
        num_map = {} # vale : index Hashmap
        for i, nums in enumerate(num):
            diff = target - nums 

            if diff in num_map:
                return [num_map[diff], i] #return first index, second index

            num_map[nums] = i    