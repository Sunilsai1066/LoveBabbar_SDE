"""
Time - O(n)
Space - O(1)
1 Pass Solution
"""
def getMinMax( a, n):
    Min,Max = float("inf"),float("-inf")
    for num in a:
        if(num < Min):
            Min = num
        if(num > Max):
            Max = num
    return Min,Max
