from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        start, end = 0, len(s1)

        freqMapS1 = Counter(s1)
        freqMapS2 = Counter(s2[start:end])

        while end <= len(s2):
            if freqMapS1 == freqMapS2:
                return True

            if end == len(s2):
                break

            freqMapS2[s2[start]] -= 1
            if freqMapS2[s2[start]] == 0:
                del freqMapS2[s2[start]]

            freqMapS2[s2[end]] += 1

            start += 1
            end += 1

        return False
