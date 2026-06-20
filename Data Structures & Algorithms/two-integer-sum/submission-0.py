class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        positions["first"] = 0
        positions["second"] = 0

        for index in range(len(nums)):
            for j in range(index + 1, len(nums)):
                if nums[index] + nums[j] == target:
                    positions["first"] = index
                    positions["second"] = j
  
        return [positions["first"], positions["second"]]
