class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,maxLength=0,0,0
        n=len(s)
        hashLen=256
        hash=[-1]*256

        while(r<n):
            if hash[ord(s[r])]!=-1:
                if hash[ord(s[r])]>=l:
                    l=hash[ord(s[r])]+1
            maxLength=max(maxLength,r-l+1)
            hash[ord(s[r])]=r
            r=r+1
        return maxLength



        