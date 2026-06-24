class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashlen=256
        # s_len={}
        # t_len={}
        # for i in range(hashlen):
        #     s_len[i]=0
        #     t_len[i]=0
        # for first in range(len(s)):
        #     s_len[ord(s[first])]=s_len.get(ord(s[first]))+1
        # for second in range(len(t)):
        #     t_len[ord(t[second])]=t_len.get(ord(t[second]))+1
        # for num in range(hashlen):
        #     if s_len.get(num)!=t_len.get(num):
        #         return False
        # return True

        # return sorted(s)==sorted(t)

        count={}
        if len(s)!=len(t):
            return False
        for c in s:
            count[c]=count.get(c,0)+1
        for c in t:
            count[c]=count.get(c,0)-1
        for value in count.values():
            if value!=0:
                return False
        return True

        
        