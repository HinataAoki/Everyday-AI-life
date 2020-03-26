# -*- coding: utf-8 -*-

'''
入力 : x1,x2
隠れ層 : O1,O2
出力 : Output
誤差 : Error
バイアス : b
重み : w[どの層, どこから, どこへ]
E = (y - Output)^2
'''
#import
import numpy as np
import random

#Setting
Input_data = np.array([[0,0,0],
                        [1,0,1],
                        [0,1,1],
                        [1,1,0]])

data_num = Input_data.shape[0]

epochs = 100000
alpha = 0.1

def Sig(x):
    return 1 / (1 + np.exp(-x))

'''
b11 = random.random()
b12 = random.random()
w111 = random.random()
w121 = random.random()
w112 = random.random()
w122 = random.random()
b21 = random.random()
w211 = random.random()
w221 = random.random()
'''
b11 = 5.167963838084365
b12 = -2.10799775474613
w111 = -3.464187552824741
w121 = -3.464346831411482
w112 = 5.222472800434783
w122 = 5.222645505343026
b21 = -18.351512325727775
w211 = 12.827093676132547
w221 = 12.340065177372864

print("b11:",b11)
print("b12:",b12)
print("w111:",w111)
print("w121:",w121)
print("w112:",w112)
print("w122:",w122)
print("b21:",b21)
print("w211:",w211)
print("w221:",w221)

for j in range(epochs):
    for i in range(data_num):
        x1 = Input_data[i][0]
        x2 = Input_data[i][1]
        y = Input_data[i][2]
        
        #Forward Propagation
        Z1 = b11 + x1*w111 + x2*w121
        Z2 = b12 + x1*w112 + x2*w122

        O1 = Sig(Z1)
        O2 = Sig(Z2)

        Z = b21 + O1*w211 + O2*w221

        Output = Sig(Z)

        Error = (y - Output)**2
        #differential
        dw111 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x1
        dw121 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x2
        db11 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))
        dw112 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x1
        dw122 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x2
        db12 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))
        dw211 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O1
        dw221 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O2
        db21 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))
        
        

        #Gradient Descent / Steepest Descent
        w111 -= alpha*(dw111)
        w121 -= alpha*(dw121)
        b11 -= alpha*(db11)
        w112 -= alpha*(dw112)
        w122 -= alpha*(dw122)
        b12 -= alpha*(db12)
        w211 -= alpha*(dw211)
        w221 -= alpha*(dw221)
        b21 -= alpha*(db21)    

x1 = np.array([[0,0,1,1]])
x2 = np.array([[0,1,0,1]])

#Forward Propagation
Z1 = b11 + x1*w111 + x2*w121
Z2 = b12 + x1*w112 + x2*w122

O1 = Sig(Z1)
O2 = Sig(Z2)

Z = b21 + O1*w211 + O2*w221

Output = Sig(Z)

print(Output)

print("b11:",b11)
print("b12:",b12)
print("w111:",w111)
print("w121:",w121)
print("w112:",w112)
print("w122:",w122)
print("b21:",b21)
print("w211:",w211)
print("w221:",w221)