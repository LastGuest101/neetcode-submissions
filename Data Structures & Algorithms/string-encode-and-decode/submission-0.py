class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            for c in s:
                word = word + c
            word = word + "é"
        return word

    def decode(self, s: str) -> List[str]:
        return s.split("é")[:-1]
