class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        array_top_k = []
        
        counts = collections.Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            array_top_k.append(sorted_counts[i][0])

        return array_top_k