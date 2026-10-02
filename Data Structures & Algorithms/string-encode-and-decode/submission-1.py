class Solution:
    def encode(self, strs: List[str]) -> str:
        encded_string = ""
        for stri in strs:
            encded_string += str(len(stri)) + "#" + stri

        return encded_string

    def decode(self, s: str) -> List[str]:
        decded_strs = []
        stri = ""
        size = ""
        index = 0
        while index < len(s):
            char = s[index]

            if char != "#":
                size += char
                index += 1
            else:
                length = int(size)
                stri = s[index + 1 : index + 1 + length]
                decded_strs.append(stri)
                index = index + 1 + length
                size = ""

        return decded_strs
