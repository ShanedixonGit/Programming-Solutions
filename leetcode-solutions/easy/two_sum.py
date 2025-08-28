from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        # First pass: build hashmap of number -> index
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        # Second pass: check for complements (the second number to reach target)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
        
"""
if __name__ == "__main__":
    # Local testing
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))   # [0, 1] (order may vary)
    print(solution.twoSum([3, 2, 4], 6))        # [1, 2]
    print(solution.twoSum([3, 3], 6))           # [0, 1]
"""