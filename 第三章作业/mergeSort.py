#归并排序
import numpy as np
import math
import time
def mergeSort(arr):
    L=len(arr)
    if(L<2):#若
        return arr
    gap = math.floor(L/2)
    left = arr[0:gap]
    right = arr[gap:L]#分治
    return merge(mergeSort(left),mergeSort(right))
def merge(left,right):
    result=[]
    while(len(left)>0 and len(right)>0):
        if left[0]<=right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    while(len(left)):#剩下的已经保证是顺序了，依次插入
        result.append(left[0])
        del left[0]
    while(len(right)):
        result.append(right[0])
        del right[0]  
    return result
# a=[1,3,5,7,2,4,6,8,3,4,5,61,123,4,2,72,4,9,223,4]
n=200000
a=np.random.rand(n).tolist()
tic=time.time()
b=mergeSort(a)
toc=time.time()
d=toc-tic
print(b)
print('数组长度为：',n,'。耗费时间为：',d,'s')