class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups_anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups_anagrams[key].append(word)

        return list(groups_anagrams.values())    