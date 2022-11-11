import random
import time

def selection_sort(alist):
    for i in range(len(alist)-1):
        minSpot = i 
        for j in range(i+1, len(alist)):
            if alist[j] < alist[minSpot]:
                minSpot = j
        if minSpot != i:
            swap(alist, i, minSpot)
    
def swap(alist, i, j):
    '''funciton that swaps things in list alist between i and j'''
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

def insertion_sort(alist):
    '''sortedList = [alist[0]]
    for i in range(1, len(alist)):
        for j in range(len(sortedList)-1, -1, -1):
            if alist[i] < sortedList[j]:
                sortedList.insert(j, alist[i])'''
    for i in range(1, len(alist)):
        item = alist[i]
        j = i
        while j>0 and alist[j-1]>item:
            alist[j] = alist[j-1]
            j-=1
        alist[j]=item 
        
def merge_sort(alist):
    mid = len(alist)//2
    left = alist[:mid]
    merge_sort(left)
    right = alist[mid:]
    merge_sort(right)
    return merge(alist, left, right)


def merge(alist, left, right):
    i = j = k = 0
    while i < len(left) and j<len(right):
        if left[i]<right[j]:
            alist[k] = left[i]
            i+=1
        else: 
            alist[k] = right[i]
            j+=1
        k+=1
    while i<len(left):
        alist[k] = left[i]
        k+=1 
        i+=1 
    while j<len(right):
        alist[k] = right[j]
        j+=1 
        k+=1
    return alist


    
    
   


