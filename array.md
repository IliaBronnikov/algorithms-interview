# Array

+ [Move Zeroes](#move-zeroes)

## Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
    if sum(nums) == 0:
        return nums
    while nums[0] == 0 and len(nums) != 1:
        nums.append(nums.pop(0))
    for i in range(len(nums)):
        while nums[i] == 0:
            nums.append(nums.pop(i))
    return nums
```

