
#6.2
#
# cost=[n,n]
import numpy as np
import matplotlib.pyplot as plt
import copy
def computeFee(solu):
    fee=0
    if len(solu)>N or max(solu)>=N:
        return False
    for i in range(0,len(solu)):
        fee+=cost[i,solu[i]]
    return fee
def minFee():
#solu为当前决策序列
#cost是一个n x n的矩阵，cij表示第i个工作给第j个人完成所需要的费用
    global bestFee
    global feeSet
    global soluSet
    global cost
    X=[0 for i in range(0,N)]
    k=0
    X[k]=-1
    while k>=0:
        X[k]+=1
        while X[k]<N and computeFee(X)>bestFee:
            X[k]+=1#转到下一个工人
        if X[k]<= N-1:
            if k==N-1:
                # print(X)
                #需要深拷贝
                soluSet.append(copy.deepcopy(X))
                bestFee=computeFee(X)
                feeSet.append(bestFee)
            else:
                k+=1#开启下一个任务
                X[k]=-1
        else:
            k-=1
    print('价格矩阵为：\n',cost)
    idx=feeSet.index(bestFee)
    print('最优解为',soluSet[idx])
    print('最优解值为',feeSet[idx])
#global
#如果递归函数传递可用人编号集，则回溯的时候不好操作，需要用全局标记
cost=np.array([[1,3,3],[3,1,2],[1,3,2]])
N=cost.shape[0]
bestFee=1e8
soluSet=[]#解集
feeSet=[]
minFee()