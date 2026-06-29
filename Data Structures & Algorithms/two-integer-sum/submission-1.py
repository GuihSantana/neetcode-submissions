class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        positions["first"] = 0
        positions["second"] = 0

        for index in range(len(nums)):
            for next_index in range(index + 1, len(nums)):
                if nums[index] + nums[next_index] == target:
                    positions["first"] = index
                    positions["second"] = next_index

        return [positions["first"], positions["second"]]     
                