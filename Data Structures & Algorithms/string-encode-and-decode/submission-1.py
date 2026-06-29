class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, word = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            word.append(str(sz))
            word.append(',')

        word.append('#')
        word.extend(strs)      


        return ''.join(word)    


    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        sizes, word, i = [], [], 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1

        i += 1    

        for sz in sizes:
            word.append(s[i:i + sz])
            i += sz

        return word        

