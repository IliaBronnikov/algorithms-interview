# Array

+ [Move Zeroes](#move-zeroes)
+ [Summary Ranges](#summary-ranges)

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

## Summary Ranges

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums

https://leetcode.com/problems/summary-ranges/

```python
def summaryRanges(self, nums: List[int]) -> List[str]:
    out = []
    if not nums:
        return out
    if len(nums) == 1:
        out.append(str(nums[0]))
        return out
    start = nums[0]
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i] == 1:
            continue
        else:
            if nums[i] == start:
                out.append(str(nums[i]))
                start = nums[i+1]
            else:
                out.append(str(start) + "->" + str(nums[i]))
                start = nums[i+1]
    if nums[-1]-nums[-2] == 1:
        out.append(str(start) + "->" + str(nums[-1]))
    else:
        out.append(str(nums[-1]))
    return out
```