# -*- coding:UTF-8 -*

def vow_sum(target, array):
    i = 0
    j = len(array)-1
    while (i<j):
        sum = array[i]+array[j]
        if sum == target:
            return i,j
        elif sum < target:
            i+=1
        else:
            j-=1
    return None

