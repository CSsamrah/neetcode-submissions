class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag=[]
        size=len(strs)
        visited=[False] * size
        
        for i in range(0,size):
            if visited[i]:
                continue
            group=[strs[i]]
            visited[i]=True
            for j in range(i+1,size):
                if not visited[j] and sorted(strs[i])==sorted(strs[j]):
                    group.append(strs[j])
                    visited[j]=True
            anag.append(group)
        return anag
                


        