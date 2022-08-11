#
import numpy as np
import math
class Node:
    def __init__(self,Max=None,i=None,j=None,left=None,right=None):
        self.Max=Max
        self.i=i
        self.j=j
        self.left=left
        self.right=right
    """
        每个节点都有left到right的最大子段和以及对应的索引（在全局数组内）
        i/j是这个子段在数组的全局索引
    """
def MaxSub(message):
    if message.left==message.right:
        L=message.left
        R=message.right
        node=Node(arr[L],L,R,L,R)
        return node;
    gap=math.floor((message.left+message.right)/2)
    nodeL=Node(None,None,None,message.left,gap)
    nodeR=Node(None,None,None,gap+1,message.right)
    return merge(MaxSub(nodeL),MaxSub(nodeR))
def merge(nodeL,nodeR):
#记录有left/right最大字串和以及对应的索引
    #计算中间的部分
    global arr
    sumL=0
    sumaL=-9e6
    i_=0
    for i in range(nodeL.right,nodeL.left-1,-1):
    #需要从中间算起，因为第三种情况一定横跨左右分界线
        sumL+=arr[i]
        if sumaL<=sumL:
            sumaL=sumL
            i_=i
    sumR=0
    sumaR=-9e6
    j_=0
    for i in range(nodeR.left,nodeR.right+1):
        sumR+=arr[i]
        if sumaR<=sumR:
            sumaR=sumR
            j_=i
    s=sumaL+sumaR
    if s<nodeL.Max:#中间的不如左边
        s=nodeL.Max
        i_=nodeL.i
        j_=nodeL.j
    #计算中间区域的最大子集和
    if s<nodeR.Max:
        s=nodeR.Max
        i_=nodeR.i
        j_=nodeR.j
    result=Node(s,i_,j_,nodeL.left,nodeR.right)
    return result
#global
arr=[5,31,-35,100,-5,-2,10,-3,1,-5,6,-6,-10]
node=Node(None,None,None,0,len(arr)-1)
node_=MaxSub(node)
print('给定数组为：{',arr,'}')
print('最大子段和为',node_.Max)
print('最大子段为第',node_.i,'到第',node_.j,'个元素')