class Solution(object):
    def consecutiveNumbersSum(self, N):
        result = 1
        while N % 2 == 0:
            N /= 2
        i = 3
        while i*i <= N:
            count = 0
            while N % i == 0:
                N /= i
                count += 1
            result *= count+1
            i += 2
        if N > 1:
            result *= 2
        return result
val=Solution()
n=int(input())
print(val.consecutiveNumbersSum(n))
