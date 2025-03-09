
'''
Will contain my answers and explanations to Easy Q's
'''

#2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)
    #(n & 1) will check if Least Significant Bit (LSB) of n is 1 and if it is will shift bits of n one to the left 
    # example 5 will turn into 10, but if n is even, it will not shift/stay the same

