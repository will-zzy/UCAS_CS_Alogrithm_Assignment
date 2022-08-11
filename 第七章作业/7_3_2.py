# 7.3最佳调度问题
import numpy as np
import math
import copy
class Node:
    def __init__(self,Parent=None,Level=None,Solve=None,Time=None):
        self.Parent=Parent#父节点
        self.Level=Level#所在任务编号
        self.Solve=Solve#所在任务给哪台机器
        self.Time=Time#当前决策需要花费的时间(所有机器花费最长的时间)
def computeTime(solve):#计算当前决策所需要的时间，若只用该值，几乎只能剪掉叶节点
#但是针对该问题不好定义一个比真实下界还要小的下界来作为判断是否应该剪枝的值
    global K,t
    time=[0 for i in range(0,K)]
    for i in range(0,len(solve)):
        if solve[i]<0:
            continue
        time[solve[i]]+=t[i]
    return max(time)
def getNewnode(E,k):#生成活节点的子节点
    a=Node(E,E.Level+1,copy.deepcopy(E.Solve),None)
    a.Solve[E.Level+1]=k
    a.Time=computeTime(a.Solve)
    EL.append(a)
def Shortest():#取出优先队列中time最小的节点
    idx=-1
    temp=1e5
    for i in range(0,len(EL)):
        if temp > EL[i].Time:
            temp=EL[i].Time
            idx=i
    a=EL[idx]
    del EL[idx]
    return a
def minTime():
    global t,K,bestT,EL,N,soluSet
    E=Node(None,-1,[-1 for i in range(0,N)],0)
    EL.append(E)
    count=0
    while True:
        count+=1
        L=E.Level+1
        if L==N:
            if bestT>E.Time:
                bestT=E.Time#到了叶节点才更新
                soluSet.append(copy.deepcopy(E))
        else:#E为中间节点
            if E.Time <= bestT:#如果该节点可活
                for i in range(0,K):
                    getNewnode(E,i)
        if len(EL)==0:
            break
        E=Shortest()
    for i in range(0,len(soluSet)):
        print('共有',K,'台机器')
        print('任务时间数组为',t)
        print('最优解为:',np.reshape(soluSet[i].Solve,[1,N])+1)
        print('最短时间为:',soluSet[i].Time)
EL=[]#活节点表
soluSet=[]#最优解集
t=[5,12,6,4,9,6,3,15]#任务时间数组
K=4#机器数
N=len(t)
bestT=1e5#下界
minTime()
