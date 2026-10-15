from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = Counter(t)
        window = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                windowLen = r - l + 1

                if windowLen < resLen:
                    res = [l, r]
                    resLen = windowLen

                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                l += 1

        l, r = res

        if resLen == float("inf"):
            return ""

        return s[l : r + 1]
