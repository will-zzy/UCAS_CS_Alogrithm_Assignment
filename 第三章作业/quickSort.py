#快速排序
import numpy as np
import time
def QS(arr,left,right):
    L=len(arr)
    if left<right:
        partitionIndex=partition(arr,left,right)#分区操作
        QS(arr,left,partitionIndex)
        QS(arr,partitionIndex+1,right)
    return arr
def partition(arr,left,right):
    privot = left#基准值
    index=privot+1
    for i in range(index,right+1):
        if arr[i]<arr[privot]:
            swap(arr,index,i)
            index+=1
    swap(arr,index-1,privot)#最后将基准值排在左边数组的最后，因为已经可以确定该元素是最大了
    return index-1
def swap(arr,i,j):
    count=arr[i]
    arr[i]=arr[j]
    arr[j]=count
n=200000
a=np.random.rand(n).tolist()
tic=time.time()
left=0
right=len(a)-1
b=QS(a,left,right)
toc=time.time()
d=toc-tic
print(b)
print('数组长度为：',n,'。耗费时间为：',d,'s')
