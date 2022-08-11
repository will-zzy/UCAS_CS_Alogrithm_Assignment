# haffman coding
import numpy as np
import math
import time
import copy#调用深拷贝
from matplotlib import pyplot as plt
#全局变量
r=0.2
class Node:
    def __init__(self,label=None,data=None,pnext1=None,pnext2=None):
        self.label=label
        self.data=data
        self.next=[]
        # self.next.append(pnext1)#左子节点
        # self.next.append(pnext2)#右子节点
    #label为该节点的标签(如果为叶子节点)
    #data为该节点的数值(如果为中间节点)
    #pnext为该节点的儿子节点(如果为中间节点)
def myHaffman(arr,fre,node):
#arr为编码序列，fre为对应的频数
#自底向上的
    if len(node)==1:#终止条件
        return node[0]
    idx=sorted(range(len(fre)),key=lambda k:fre[k])
    #按频数新一轮从小到大排序
    fre_=[]
    arr_=[]
    node_=[]
    for i in range(0,len(idx)):
        fre_.append(fre[idx[i]])
        arr_.append(arr[idx[i]])    
        node_.append(node[idx[i]])
    #手动深拷贝，顺便排序
    node1=Node(arr_[0],fre_[0])
    node2=Node(arr_[1],fre_[1])
    for i in range(0,len(node_[0].next)):
        node1.next.append(node_[0].next[i])
    for i in range(0,len(node_[1].next)):
        node2.next.append(node_[1].next[i])
    mid=node1.data+node2.data
    nodeF=Node()
    nodeF.data=mid
    nodeF.next.append(node1)
    nodeF.next.append(node2)
    arr_.append(None)
    fre_.append(mid)
    node_.append(nodeF)
    del arr_[0:2]
    del fre_[0:2]
    del node_[0:2]
    return myHaffman(arr_,fre_,node_)
def detectTree(nod,n,idx):
    if nod.next==[]:
        return n
    n_=n+1
    for i in range(0,len(nod.next)):
        x=idx[0]+5*r*(-1)**int(i+1)
        label=1
        if nod.next[i].next==[]:
            x=idx[0]+(3*r)*(-1)**int(i+1)
            label=0#该子节点为叶节点
        y=idx[1]-5*r
        # 画树节点之间连线
        plt.plot([x,idx[0]],[y,idx[1]])
        plt.text((x+idx[0])/2+(-1)**int(i+1)*r/4,(y+idx[1])/2+r/2,str(i))
        if label==0:#画叶子节点
            rect=plt.Rectangle((x-r/2,y-r/2),r,r,color='coral',alpha=1)
            ax1=fig.add_subplot(111)
            ax1.add_patch(rect)
            s=nod.next[i].label+":"+str(nod.next[i].data)
            plt.text(x-r/2,y-r/4,s)
        else:#画内部节点
            circle=plt.Circle((x,y),r,color='cyan',alpha=1)
            ax=fig.add_subplot(111)
            ax.add_patch(circle)
            s=str(nod.next[i].data)
            plt.text(x-r/4,y-r/4,s)            
        a=nod.next[i]
        detectTree(a,n_,[x,y])
def main(arr,fre):
    node=[]
    for i in range(0,len(arr)):
        node.append(Node(arr[i],fre[i]))
    h=myHaffman(arr,fre,node)
    return h
def fib(n):#{
    if n<=2 :
        return 1;
    else:
        return fib(n-1)+fib(n-2);
fre=[]
arr=[]
for i in range(1,30):
    arr.append(str(fib(i)))
    fre.append(fib(i))
# arr=['a','b','c','d','e','f','g','h','']
# fre=[45,13,12,16,5,9]
h=main(arr,fre)
fig=plt.figure()
plt.title('Haffman Tree')
detectTree(h,0,[8,8])
fig.tight_layout()
plt.show()