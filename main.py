from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Dict for storing idx and number
    num_map = {}
    
    for i, num in enumerate(nums):
    # Calculate the number that, when added to the current number, equals the target.
        comp = target - num

        # Check if that number already in num_map.
        if comp in num_map:
            return [num_map[comp], i]

        #  Store the current number and its idx in the num_map.
        num_map[num] = i