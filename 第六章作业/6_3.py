
#6.2
#
# cost=[n,n]
import numpy as np
import matplotlib.pyplot as plt
import copy
def computeTime(solu):
    Time=[0 for i in range(0,K)]
    if len(solu)>N or max(solu)>=K:
        return False
    for i in range(0,len(solu)):
        Time[solu[i]]+=t[i]
    return max(Time)
def boundPre():#先用局部贪心求解一个上界
    time=[0 for i in range(0,K)]
    for i in range(0,N):
        time[time.index(min(time))]+=t[i]
    return max(time)
def minTime():
    global bestTime
    global timeSet
    global soluSet
    #x[k]表示第k个任务由x[k]个机器完成
    X=[0 for i in range(0,N)]
    k=0
    count=0
    X[k]=-1
    bPre=boundPre()
    while k>=0:
        X[k]+=1
        while X[k]<K and computeTime(X)>bestTime:
            X[k]+=1#转到下一个机器
        if X[k]<= K-1:
            if k==N-1:
                #需要深拷贝
                soluSet.append(copy.deepcopy(X))
                count +=1
                # if bestTime>computeTime(X):
                    # bestTime=computeTime(X)
                if bestTime>min([computeTime(X),bPre]):
                    bestTime=min([computeTime(X),bPre])#只有当找到一个解时，上界才进行更新
                timeSet.append(computeTime(X))
            else:
                k+=1#开启下一个任务
                X[k]=-1
        else:
            k-=1#回溯
    print('费用矩阵为：\n',t)
    # print(soluSet)
    idx=timeSet.index(bestTime)
    print('最优解为',soluSet[idx])
    print('最优解值为',timeSet[idx])
#global
t=[5,12,7,18,9,6,3,15,9,15,3,2,3,5]
N=len(t)
K=3
bestTime=1e8
soluSet=[]#解集
timeSet=[]
minTime()