# -*- coding:UTF-8 -*-

## search from a sorted array: O(log n)
# pay special attention to the corner cases in practical

#
# import bisect.bisect
# index = bisect.bisect(ls,a)

def binarysearch_noduplicate(ls, target):
    length = len(ls)
    low = 0
    high = length-1
    while(low<=high): # there is a '=', becasue have to check if when mid=low=high, mid ?= target
        mid = int((low + high) / 2)
        if mid < target:
            low = mid + 1
        elif mid > target:
            high = mid - 1
        else:
            return mid

def binarysearch_ifduplicate_findleftmost(ls, target):
    length = len(ls)
    low = 0
    high = length - 1
    while (low < high):  # there is NO '=', because if low <= high, loop may not end
        mid = int((low + high) / 2)
        if mid < target:
            low = mid + 1
        else:
            high = mid # means mid >= target, low is fixed once mid == target
    return low #may not find the ans, need check in call function (higher layer)


# 69 sqrt
# 1st time with bug
def _sqrt(n):
    if n<0:
        return None

    low = 0
    high = n
    mid = 0
    while(low<=high):
        mid = int((low+high)/2)
        sqrt = n/mid
        if mid < sqrt:
            low = mid+1
        elif mid > sqrt:
            high = mid-1
        else:
            return mid
    return high

# float sqrt
# acc 0.0001
def float_sqrt(x):
    if x<0:
        return None

    low = 0.0
    high = x
    mid = 0.0
    #mid = low + (high-low)/2
    while(high-low>0.0001):
        mid = low + (high - low) / 2
        k = x/mid
        if mid-k>=0.0 and mid-k<=0.0001:
            return mid
        elif mid-k>0.0001:
            high = mid
        else:
            low = mid
    return mid

# Newton's Law
# f(x)=x^2-a,f'(x)=2x.
# x1=x0-f(x0)/f'(x0)
# x1=x0-(x0^2-a)/2x0=(x0+a/x0)/2

# 774 Find Smallest Letter Greater Than Target (Easy)
# notes:
# duplicates
# wrap around

def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    length = len(letters)
    low = 0
    high = length-1
    #mid = 0
    while (low<high):
        mid = int((low+high)/2)
        if letters[mid]>target:
            high = mid-1
        #elif letters[mid]<=target:
        else:
            low = mid+1

    '''
    if letters[low] > target:
        return letters[low]
    else:
        if low == length - 1:
            return letters[0]  # end
        else:
            return letters[low + 1]  # begin
    '''

    sollution = 0
    if letters[low] > target:
        sollution = low
    else:
        sollution = low+1

    return letters[sollution%len(letters)]

# or use bisect

def nextGreatestLetter2(letters, target):
    import bisect.bisect
    index = bisect.bisect(letters,target)
    return (letters[index%len(letters)])










if __name__ =='__main__':
    print(_sqrt(15))
    print(float_sqrt(16))
    print(nextGreatestLetter(["c","f","j"],"c"))
    print()
