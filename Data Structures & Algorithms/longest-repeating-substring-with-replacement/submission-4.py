class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}

        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxf = max(maxf, freqMap.get(s[r], 0))

            while (r - l+1 - maxf > k):
                freqMap[s[l]] -= 1
                l+=1
            
            res = max(r-l+1, res)
        
        return res