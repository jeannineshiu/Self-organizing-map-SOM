#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.setrecursionlimit(10000)
import os
from PyQt5.QtWidgets import *
from form import Ui_Form    #MyFirstUI 是你的.py檔案名字

#for openfile
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#drawing
import random
import matplotlib  
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


import numpy as np
import pylab as pl

class SOM(object):
    def __init__(self, X, output, iteration, batch_size):
        """
        :param X: 形状是N*D， 输入样本有N个,每个D维
        :param output: (n,m)一个元组，为输出层的形状是一个n*m的二维矩阵
        :param iteration:迭代次数
        :param batch_size:每次迭代时的样本数量
        初始化一个权值矩阵，形状为D*(n*m)，即有n*m权值向量，每个D维
        """
        self.X = X
        self.output = output
        self.iteration = iteration
        self.batch_size = batch_size
        self.W = np.random.rand(X.shape[1], output[0] * output[1])
        #print (self.W.shape)
 
    def GetN(self, t):
        """
        :param t:时间t, 这里用迭代次数来表示时间
        :return: 返回一个整数，表示拓扑距离，时间越大，拓扑邻域越小
        """
        a = min(self.output)
        return int(a-float(a)*t/self.iteration)
 
    def Geteta(self, t, n):
        """
        :param t: 时间t, 这里用迭代次数来表示时间
        :param n: 拓扑距离
        :return: 返回学习率，
        """
        return np.power(np.e, -n)/(t+2)
 
    def updata_W(self, X, t, winner):
        N = self.GetN(t)
        for x, i in enumerate(winner):
            to_update = self.getneighbor(i[0], N)
            for j in range(N+1):
                e = self.Geteta(t, j)
                for w in to_update[j]:
                    self.W[:, w] = np.add(self.W[:,w], e*(X[x,:] - self.W[:,w]))
 
    def getneighbor(self, index, N):
        """
        :param index:获胜神经元的下标
        :param N: 邻域半径
        :return ans: 返回一个集合列表，分别是不同邻域半径内需要更新的神经元坐标
        """
        a, b = self.output
        length = a*b
        def distence(index1, index2):
            i1_a, i1_b = index1 // a, index1 % b
            i2_a, i2_b = index2 // a, index2 % b
            return np.abs(i1_a - i2_a), np.abs(i1_b - i2_b)

        ans = [set() for i in range(N+1)]
        for i in range(length):
            dist_a, dist_b = distence(i, index)
            if dist_a <= N and dist_b <= N: ans[max(dist_a, dist_b)].add(i)
        return ans
 
 
    def train(self):
        """
        train_Y:训练样本与形状为batch_size*(n*m)
        winner:一个一维向量，batch_size个获胜神经元的下标
        :return:返回值是调整后的W
        """
        count = 0
        while self.iteration > count:
            train_X = self.X[np.random.choice(self.X.shape[0], self.batch_size)]
            normal_W(self.W)
            normal_X(train_X)
            train_Y = train_X.dot(self.W)
            winner = np.argmax(train_Y, axis=1).tolist()
            self.updata_W(train_X, count, winner)
            count += 1
        return self.W
 
    def train_result(self):
        normal_X(self.X)
        train_Y = self.X.dot(self.W)
        winner = np.argmax(train_Y, axis=1).tolist()
        #print (winner)
        return winner


# In[3]:


#主程式function
def normal_X(X):
    """
    :param X:二维矩阵，N*D，N个D维的数据
    :return: 将X归一化的结果
    """
    N, D = X.shape
    for i in range(N):
        temp = np.sum(np.multiply(X[i], X[i]))
        X[i] /= np.sqrt(temp)
    return X


def normal_W(W):
    """
    :param W:二维矩阵，D*(n*m)，D个n*m维的数据
    :return: 将W归一化的结果
    """
    for i in range(W.shape[1]):
        temp = np.sum(np.multiply(W[:,i], W[:,i]))
        W[:, i] /= np.sqrt(temp)
    return W


# In[4]:


class AppWindow(QWidget):
    
    dataset = []
    numm = 0
    dataset_old = []
    C = []           #original classification result
    D = []           #normalized classification result
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #1.open file
        self.ui.btopenfile.clicked.connect(self.openbt_Click)
        self.ui.btrun.clicked.connect(self.run)
        
    def openbt_Click(self):
        a = []
        self.dataset = []
        self.dataset_old = []
        self.C = []
        self.D = []
        self.numm = 0
        
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            f = open(filenames[0], 'r') 
            #show filename
            filename = os.path.basename(filenames[0])
            self.ui.filenamelabel.setText(filename)
            
            with f:
                line = f.read()
                #print(line)

            f.close()

            ##process data
            a = line.split()
            self.dataset = np.mat([[float(a[i]), float(a[i+1])] for i in range(0, len(a)-1, 3)])
            #print(self.dataset)
            #print(self.dataset.shape[0])
            #print(self.dataset.shape[1])
            self.numm = self.dataset.shape[0]
            
            
    def run(self):
        
        self.dataset_old = self.dataset.copy()
        som = SOM(self.dataset, (15, 15), 1, self.numm)
        som.train()
        res = som.train_result()
        classify = {}
        for i, win in enumerate(res):
            if not classify.get(win[0]):
                classify.setdefault(win[0], [i])
            else:
                classify[win[0]].append(i)

        
        for i in classify.values():
            self.C.append(self.dataset_old[i].tolist())
            self.D.append(self.dataset[i].tolist())
            
        ##draw the result
        self.drawO(self.C)
        self.drawN(self.D)
        
    def drawO(self,A):
        self.ui.mplwidget1.canvas.ax.clear()
        colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm','gray','rosybrown','bisque','darkkhaki','darkturquoise','plum','purple','lightcoral']
        for i in range(len(A)):
            coo_X = []  #x坐标列表
            coo_Y = []  #y坐标列表
            for j in range(len(A[i])):
                coo_X.append(A[i][j][0])
                coo_Y.append(A[i][j][1])
            self.ui.mplwidget1.canvas.ax.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

        self.ui.mplwidget1.canvas.ax.legend(loc='upper right')
        self.ui.mplwidget1.canvas.draw()
        
    def drawN(self,A):
        self.ui.mplwidget2.canvas.ax.clear()
        colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm','gray','rosybrown','bisque','darkkhaki','darkturquoise','plum','purple','lightcoral']
        for i in range(len(A)):
            coo_X = []  #x坐标列表
            coo_Y = []  #y坐标列表
            for j in range(len(A[i])):
                coo_X.append(A[i][j][0])
                coo_Y.append(A[i][j][1])
            self.ui.mplwidget2.canvas.ax.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)

        self.ui.mplwidget2.canvas.ax.legend(loc='upper right')
        self.ui.mplwidget2.canvas.draw()
        

            


# In[5]:


## main function
if __name__ == "__main__":
    app = QApplication(sys.argv)  
    MainWindow = AppWindow()
    MainWindow.show()
    sys.exit(app.exec_())  

