class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        #LENGTHS ARE SAME
        s_count, t_count = {}, {}
        for i in range(len(s)): 
            
            if s[i] not in s_count:
                s_count[s[i]] = 0
            if t[i] not in t_count:
                t_count[t[i]] = 0

            s_count[s[i]] += 1
            t_count[t[i]] += 1

        print(set(s_count.items()))
        print(set(t_count.items()))
        if set(s_count.items()) != set(t_count.items()):
            return False

        return True

