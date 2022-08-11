#6.5
#
#
import numpy as np
import matplotlib.pyplot as plt
import copy
def minWeight(depth):
    global N,M,BW,cw,cc,X,minX
    if depth==N:#到达叶子节点
        if cw<BW and cc<=CB:
            BW=cw
            minX=copy.deepcopy(X)
        return
    for i in range(0,M):#当且仅当满足两个条件才扩展子节点
        cw+=W[depth,i]
        cc+=C[depth,i]
        X[depth]=i
        if cw<BW and cc <=CB:
            minWeight(depth+1)
        cw-=W[depth,i]#回溯时需要回复枝的信息
        cc-=C[depth,i]
N=4
M=3
BW=1e4
cw=0
cc=0
X=np.array([0 for i in range(0,N)])
minX=np.array([0 for i in range(0,N)])
W=np.array([[2,4,1],[1,3,5],[3,4,1],[2,4,2],[8,4,3]])
C=np.array([[10,10,20],[30,50,30],[20,10,30],[20,30,40],[30,40,50]])
CB=100#价格上界
# W=np.zeros([N,M])
# C=np.zeros([N,M])
minWeight(0)
print('质量矩阵为：\n',W)
print('价格矩阵为：\n',C)
print('价格上界为：\n',CB)
print('最优解为：\n',minX)
