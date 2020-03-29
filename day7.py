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
import time

#Setting
Input_data = np.array([[0,0,0],
                        [1,0,1],
                        [0,1,1],
                        [1,1,0]])

data_num = Input_data.shape[0]

epochs = 10000
pre_epo = 1000
num_of_mult = 10
alpha = 0.1
def Sig(x):
    return 1 / (1 + np.exp(-x))

b11 = random.random()
b12 = random.random()
b13 = random.random()
w111 = random.random()
w121 = random.random()
w112 = random.random()
w122 = random.random()
w113 = random.random()
w123 = random.random()
b21 = random.random()
w211 = random.random()
w221 = random.random()
w231 = random.random()

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
print("b13:",b13)
print("w111:",w111)
print("w121:",w121)
print("w112:",w112)
print("w122:",w122)
print("w113:",w113)
print("w123:",w123)
print("b21:",b21)
print("w211:",w211)
print("w221:",w221)
print("w231:",w231)
'''
'''
for j in range(epochs):
    for i in range(data_num):
        x1 = Input_data[i][0]
        x2 = Input_data[i][1]
        y = Input_data[i][2]
        
        #Forward Propagation
        Z1 = b11 + x1*w111 + x2*w121
        Z2 = b12 + x1*w112 + x2*w122
        Z3 = b13 + x1*w113 + x2*w123

        O1 = Sig(Z1)
        O2 = Sig(Z2)
        O3 = Sig(Z3)

        Z = b21 + O1*w211 + O2*w221 + O3*w231

        Output = Sig(Z)
        if j==1:
            print(Output)
        Error = (y - Output)**2

        #differential
        dw111 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x1
        dw121 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x2
        db11 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))
        dw112 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x1
        dw122 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x2
        db12 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))
        dw113 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))*x1
        dw123 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))*x2
        db13 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))
        dw211 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O1
        dw221 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O2
        dw231 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O3
        db21 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))

        #Gradient Descent / Steepest Descent
        w111 -= alpha*(dw111)
        w121 -= alpha*(dw121)
        b11 -= alpha*(db11)
        w112 -= alpha*(dw112)
        w122 -= alpha*(dw122)
        b12 -= alpha*(db12)
        w113 -= alpha*(dw113)
        w123 -= alpha*(dw123)
        b13 -= alpha*(db13)
        w211 -= alpha*(dw211)
        w221 -= alpha*(dw221)
        w231 -= alpha*(dw231)
        b21 -= alpha*(db21)
    print("\r No.%d"%j, end='')
    

    x1 = np.array([[0,0,1,1]])
    x2 = np.array([[0,1,0,1]])
    
    #Forward Propagation
    Z1 = b11 + x1*w111 + x2*w121
    Z2 = b12 + x1*w112 + x2*w122
    Z3 = b13 + x1*w113 + x2*w123
    
    O1 = Sig(Z1)
    O2 = Sig(Z2)
    O3 = Sig(Z3)
    
    Z = b21 + O1*w211 + O2*w221 + O3*w231
    
    Output = Sig(Z)

    print("\r",Output)
'''

#優秀な奴を選ぶ 5*1000
player = []
Error_player = []
for l in range(2):
    for k in range(num_of_mult):
        sum_Error = 0
        pre_player = []
        if l == 0:
            b11 = random.random()
            b12 = random.random()
            b13 = random.random()
            w111 = random.random()
            w121 = random.random()
            w112 = random.random()
            w122 = random.random()
            w113 = random.random()
            w123 = random.random()
            b21 = random.random()
            w211 = random.random()
            w221 = random.random()
            w231 = random.random()
        else :
            b11,b12,b13,w111,w121,w112,w122,w113,w123,b21,w211,w221,w231 = player[best_player]

        for j in range(pre_epo):
            for i in range(data_num):
                x1 = Input_data[i][0]
                x2 = Input_data[i][1]
                y = Input_data[i][2]
                
                #Forward Propagation
                Z1 = b11 + x1*w111 + x2*w121
                Z2 = b12 + x1*w112 + x2*w122
                Z3 = b13 + x1*w113 + x2*w123
        
                O1 = Sig(Z1)
                O2 = Sig(Z2)
                O3 = Sig(Z3)
        
                Z = b21 + O1*w211 + O2*w221 + O3*w231
        
                Output = Sig(Z)
                #if j==1:
                    #print(Output)
                Error = (y - Output)**2
                
                #differential
                dw111 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x1
                dw121 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x2
                db11 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))
                dw112 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x1
                dw122 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x2
                db12 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))
                dw113 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))*x1
                dw123 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))*x2
                db13 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z3)*(1 - Sig(Z3))
                dw211 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O1
                dw221 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O2
                dw231 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O3
                db21 = -2*(y - Output)*Sig(Z)*(1 - Sig(Z))
        
                #Gradient Descent / Steepest Descent
                w111 -= alpha*(dw111)
                w121 -= alpha*(dw121)
                b11 -= alpha*(db11)
                w112 -= alpha*(dw112)
                w122 -= alpha*(dw122)
                b12 -= alpha*(db12)
                w113 -= alpha*(dw113)
                w123 -= alpha*(dw123)
                b13 -= alpha*(db13)
                w211 -= alpha*(dw211)
                w221 -= alpha*(dw221)
                w231 -= alpha*(dw231)
                b21 -= alpha*(db21)
                
                if j == pre_epo-1:
                    sum_Error += Error
            #print("\r No.%d"%j, end='')
        Error_player.append(sum_Error)
        pre_player += [b11,b12,b13,w111,w121,w112,w122,w113,w123,b21,w211,w221,w231]
        player.append(pre_player)
        best_player = np.argmin(Error_player)
            
            

        x1 = np.array([[0,0,1,1]])
        x2 = np.array([[0,1,0,1]])
        
        #Forward Propagation
        Z1 = b11 + x1*w111 + x2*w121
        Z2 = b12 + x1*w112 + x2*w122
        Z3 = b13 + x1*w113 + x2*w123
        
        O1 = Sig(Z1)
        O2 = Sig(Z2)
        O3 = Sig(Z3)
        
        Z = b21 + O1*w211 + O2*w221 + O3*w231
        
        Output = Sig(Z)
        
        print("\r",Output)
        print(best_player)




print("b11 = ",b11)
print("b12 = ",b12)
print("b13 = ",b13)
print("w111 = ",w111)
print("w121 = ",w121)
print("w112 = ",w112)
print("w122 = ",w122)
print("w113 = ",w113)
print("w123 = ",w123)
print("b21 = ",b21)
print("w211 = ",w211)
print("w221 = ",w221)
print("w231 = ",w231)

endtime = time.time()
#print("実行時間 : %d"%endtime-starttime)