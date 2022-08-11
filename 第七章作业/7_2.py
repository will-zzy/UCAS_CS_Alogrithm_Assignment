#7.2 0/1背包的分支定界
import numpy as np
import math
import copy
import random
class Node:
    def __init__(self,Parent=None,Level=None,Tag=None,CC=None,CV=None,CUB=None):
        self.Parent=Parent#指向父节点的指针
        self.Level=Level#节点在解空间中的深度
        self.Tag=Tag#该节点深度对应的物品那还是不拿1/0
        self.CC=CC#该节点下背包的剩余空间
        self.CV=CV#该节点下物品的价值
        self.CUB=CUB#该节点下可能达到的物品价值上界Puv,该上界≥真实上界
def LUBound(P,W,cap,cv,N,k):
    global Pvl,Pvu
    Pvl=cv#初始化下界为当前价值
    rw=cap#剩余容量
    for i in range(k-1,N):
        if rw<W[i]:
            Pvu=Pvl+rw*P[i]/W[i]#填满
            for j in range(i+1,N):
                if rw>=W[j]:
                    rw-=W[j]
                    Pvl+=P[j]#贪心
            return
        rw-=W[i]
        Pvl+=P[i]
    Pvu=Pvl
def NewNode(parent,level,tag,cap,cv,ub):
    global EL
    a=Node(parent,level,tag,cap,cv,ub)
    EL.append(a)
def Finsh(CV,ANS,N,P,W,M):
    print("价值数组为：",P)
    print("质量数组为：",W)
    print("背包容量为：",M)
    print("背包内剩余空间为",ANS.CC)
    print("背包内总价值为",ANS.CV)
    solve=[]
    for j in range(N-1,-1,-1):
        if ANS.Tag==1:
            solve.append(j+1)
        ANS=ANS.Parent
    print("应该拿的物品为：",solve)
    
def Largest():#在活结点表中取一个具有最大Pvu值的节点作为当前扩展结点
    global EL
    temp=-1
    idx=-1
    for i in range(0,len(EL)):
        if EL[i].CUB>temp:
            idx=i
            temp=EL[i].CUB
    a=EL[idx]
    del EL[idx]
    return a
def dataPre(P,W):
#按照p/w从大到小顺序排列
    P1=np.zeros([P.shape[0]])
    W1=np.zeros([W.shape[0]])
    middle=P/W
    idx=middle.argsort()
    for i in range(0,P.shape[0]):
        P1[i]=P[idx[-i-1]]
        W1[i]=W[idx[-i-1]]
    return P1,W1
def maxValue(P,W,M):
    # global P,W,EL,M
    #价值,重量,活节点表,背包容量
    global Pvl,Pvu,prev,EL,ANS
    #下界,上界
    N=P.shape[0]
    LUBound(P,W,M,0,N,1)
    # E1=Node(None,-1,None,M,0,Pvu)#生成根节点
    E=Node(None,-1,None,M,0,Pvu)#生成根节点
    EL.append(E)#将根节点加入活结点表
    prev=Pvl
    # E.CUB=Pvu
    while True:
        i=E.Level+1
        cap=E.CC
        cv=E.CV
        if i==N:
            if cv>=prev:
                prev=cv
                ANS=E
        #开始定界
        else:#E是内部节点，接下来判断哪个儿子可行
            if cap>=W[i]:#可拿，左儿子活
                NewNode(E,i,1,cap-W[i],cv+P[i],E.CUB)
                # prev=max(prev,Pvl-epsilon)
            LUBound(P,W,cap,cv,N,i+1)
            #这里更新了Pvl和Pvu为不拿第i个物品的上下界
            if Pvu>prev:
            #不拿，只要可能的上界>已知最好结果也可活
                NewNode(E,i,0,cap,cv,Pvu)
                prev=max(prev,Pvl-epsilon)
        if len(EL)==0:
            break
        E=Largest()
        if E.CUB<prev:
            break
    Finsh(cv,ANS,N,P,W,M)
# global
EL=[]#活节点表
ANS=Node()#最优解
# P=np.array([10,10,12,18])
# W=np.array([2,4,6,9])
# M=15
# P=np.array([2  ,136  ,120,8,10,12,1])
# W=np.array([0.2,17,20,2,3 ,9 ,1])
# M=16
# P=np.array([2  ,136  ,120,8,10,12,1])
# W=np.array([0.2,17,20,2,3 ,9 ,1])
# M=160
N=16
P=np.zeros(N)#价值矩阵
W=np.zeros(N)#质量矩阵
for i in range(0,N):
    P[i]=random.randint(1,30)
    W[i]=random.randint(1,30)
P,W=dataPre(P,W)
M=sum(W)/1.5#背包容量
epsilon=1e-4#极小常量
Pvl=0
Pvu=0
maxValue(P,W,M)




