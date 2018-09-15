# -*- coding:UTF-8 -*-

def sort_array(arry):
    if len(arry)==1:
        return arry
    else:
        next_arry = sort_array(arry[1:])
        return __insert(arry[0], next_arry)



def __insert(n,arry):
    l =len(arry)
    new_arry = []
    for i in range(l):
        if n>arry[i]:
            continue
        else:
            new_arry[:i]=arry[:i]
            new_arry.append(n)
            if i+1<=len(arry):
                new_arry[i+1:]=arry[i:]
            return new_arry
    new_arry = arry[:]
    new_arry.append(n)
    return new_arry

def mergesort(arry):
    '''
    if len(arry)==2:
        if arry[0]>arry[1]:
            t = arry[0]
            arry[0] = arry[1]
            arry[1] = t
            return arry
        else:
            return arry
    '''
    if len(arry)==1:
        return arry
    else:
        mid = int(len(arry)/2)
        a1=mergesort(arry[:mid])
        a2=mergesort(arry[mid:])
        new_arry = merge(a1,a2)
        return new_arry
def merge(a,b):
    la=len(a)
    lb=len(b)
    new_arry=[]
    i=0
    j=0
    idx=0
    while (i<la and j<lb):
        if a[i]<b[j]:
            new_arry.append(a[i])
            i+=1
        else:
            new_arry.append(b[j])
            j+=1
        idx+=1
    if j<lb:
        new_arry[idx:idx+(lb-j)]=b[j:]
    if i<la:
        new_arry[idx:idx+(la-i)]=a[i:]

    return new_arry

def insert_sort(a):
    if len(a)==1:
        return a
    else:
        b= insert_sort(a[1:])
        ans=insert(a[0],b)
    return ans


def insert(n,a):
    for i in range(len(a)):
        if n>a[i]:
            continue
        else:
            b=a[:i]
            b.append(n)
            b[i+1:]=a[i:]
            return b
    b = a[:]
    b.append(n)
    return b

def quick_sort(a):
    if len(a)==1:
        return a
    else:
        k = _split(a)
        quick_sort(a[:k])
        if k < len(a) - 1:
            quick_sort(a[k+1:])
        return a


def _split(a):
    x=a[-1]
    j = len(a)-1
    for i in range(len(a)-2,-1,-1):
        if x<a[i]:
            a[j]=a[i]
            a[i:j-1]=a[i+1:j]
            j-=1
    a[j]=x
    return j




if __name__ == '__main__':
    a = [5,24,3,2,1,6,7]
    #a=[2,3]
    #b = sort_array(a)
    #c = mergesort(a)
    #b=[1,3]
    #d=[2]
    #e=merge(b,d)
    b = quick_sort(a)
    print(b)


