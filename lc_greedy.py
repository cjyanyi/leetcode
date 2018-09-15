# -*- coding:UTF-8 -*-

## 1
#  can be simplified
def assign_cookies(child,cookies):
    chld = sorted(child[:])
    ck = sorted(cookies[:])

    return _assign_sorted(chld,ck)



def _assign_sorted(ch,cookies):
    if len(ch)==1:
        if cookies[0]>=ch[0]:
            return 1
        elif len(cookies)==1:
            return 0
        else:
            return _assign_sorted(ch,cookies[1:])
    if len(cookies)==1:
        if cookies[0]>=ch[0]:
            return 1
        else:
            return 0

    if cookies[0]>=ch[0]:
        return 1+_assign_sorted(ch[1:],cookies[1:])
    else:
        return _assign_sorted(ch,cookies[1:])

## 2

def non_overlapping(l):
    #end_start = {}
    #for i in range(len(l)):
        #end_start[l[i][1]]=l[i][0]

    start_end_arry = sorted(l[:], key = lambda x:x[1])

    left = start_end_arry[0][1]
    sollution = []
    sollution.append(start_end_arry[0])

    for i in range(1,len(start_end_arry)):
        if start_end_arry[i][0]>=left:
            left = start_end_arry[i][1]
            sollution.append(start_end_arry[i])
        else:
            continue
    return len(l)-len(sollution)

## 3
def burst_ballons(l):
    count = 0
    ballons = sorted(l,key=lambda x:x[1])

    left_coord = ballons[0][0]
    right_coord =ballons[0][1]
    aready_overlap = False
    for i in range(1,len(ballons)):
        if ballons[i][0]<right_coord:
            if aready_overlap==False:
                aready_overlap=True
                count+=1
            left_coord = max(left_coord,ballons[i][0])
            right_coord = min(right_coord,ballons[i][1])
        else:
            if aready_overlap==True:
                aready_overlap=False
            left_coord = ballons[i][0]
            right_coord = ballons[i][1]
    return count

def burst_ballons2(l):
    count = 1
    ballons = sorted(l,key = lambda x:x[1])

    right = ballons[0][1]
    for i in range(1,len(ballons)):
        if ballons[i][0]<=right:
            continue
        else:
            count+=1
            right = ballons[i][1]
    return count

# 406. Queue Reconstruction by Height(Medium)
# can only do brute force -^-
# O(nlog n)

def cmpor(a,b):
    return a[1] - b[1] if a[0]==b[0] else b[0] - a[0]

def queReconstruct(ls):
    #import queue
    from functools import cmp_to_key
    length = len(ls)
    if ls is None or length == 0 or len(ls[0]) ==0:
        return []

    # out-of-dated
    #ls.sort(cmp=cmpor,reverse=True)
    ls.sort(key=cmp_to_key(cmpor),reverse=True)
    result = []
    for i in range(length):
        result.insert(ls[i][1],ls[i])
    return result

def partitionStr(s):
    length = len(s)
    right = 0
    result = []
    for i in range(length-1):
        char = s[i]
        if right<s.find(char):
            result.append(i)

        # evaluate 'right'
        j=s.find(char,start=i+1)
        while (j>0 and j<length-1):
            if j>ringht:
                right = j
            j = s.find(char,start=j+1)

    return result










if __name__ == '__main__':
    child = [1,2,3]
    cookies = [1,1]
    #print(assign_cookies(child,cookies))

    l =  [ [1,2], [2,3], [3,4], [1,3] ]
    #print(non_overlapping(l))

    l = [[10,16], [2,8], [1,6], [7,12]]
    #print(burst_ballons2(l))

    l= [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    #print(queReconstruct(l))

    s='ababcbacadefegdehijhklij'
    s.find('a',__start=1)
    #print(partitionStr(s))
