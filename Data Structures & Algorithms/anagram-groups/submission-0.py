class Solution:
    def getIndex(self, c: str) -> int:
        mapping = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
        }
        
        return mapping[c]
        
        
    def toCounter(self, str_a: str) -> List[int]:
        counter = [0] * 26
        for c in str_a:
            counter[self.getIndex(c)] += 1
        return str(counter)
        
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashmap = {}
        for i in range(len(strs)):
            counter = self.toCounter(strs[i])
            if not counter in hashmap:
                hashmap[counter] = [strs[i]]
            else:
                hashmap[counter].append(strs[i])
        result = []
        for key in hashmap:
            result.append(hashmap[key])
        return result
        