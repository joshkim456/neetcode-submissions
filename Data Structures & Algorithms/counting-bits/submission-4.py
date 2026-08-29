class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)
        for digit in range(1, n+1):
            i = digit
            bits = 0
            while digit:
                bits += digit%2
                digit = digit >> 1
            output[i] = bits
        return output