class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for index_one in range(len(nums)):
            product = 1
            for index_two in range(len(nums)):
                if index_one != index_two:
                    product *= nums[index_two]
            result.append(product)        

        return result