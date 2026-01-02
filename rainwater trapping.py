# Program to find how much water is trapped between bars

def findwater(bars):
    n = len(bars)

    # store tallest bar on the left
    left = [0] * n
    # store tallest bar on the right
    right = [0] * n

    water = 0

    # left tallest
    left[0] = bars[0]
    for i in range(1, n):
        if bars[i] > left[i-1]:
            left[i] = bars[i]
        else:
            left[i] = left[i-1]

    # right tallest
    right[n-1] = bars[n-1]
    for i in range(n-2, -1, -1):
        if bars[i] > right[i+1]:
            right[i] = bars[i]
        else:
            right[i] = right[i+1]

    # calculate water
    for i in range(n):
        water += min(left[i], right[i]) - bars[i]
    return water

bars = [0,1,0,2,1,0,1,3,2,1,2,1]
print("Water :", findwater(bars))

