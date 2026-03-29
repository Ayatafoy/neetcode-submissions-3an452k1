class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        for c in s:
            if not c in s_hashmap:
                s_hashmap[c] = 1
            else:
                s_hashmap[c] += 1
        for c in t:
            if not c in t_hashmap:
                t_hashmap[c] = 1
            else:
                t_hashmap[c] += 1
        for k in s_hashmap:
            if not k in t_hashmap:
                return False
            if s_hashmap[k] != t_hashmap[k]:
                return False
        for k in t_hashmap:
            if not k in s_hashmap:
                return False
            if t_hashmap[k] != s_hashmap[k]:
                return False
        return True