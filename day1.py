# -*- coding: utf-8 -*-
'''
Sig:=Sigmoid
    =発症率（生活習慣病の）
    =1/(1+e^-(β0+β1*x1+β2*x2))
    
健康の発症率=(1-生活習慣病の発症率)
    =1-Sig
'''
#import
import numpy as np
import random
import matplotlib.pyplot as plt

#インプットデータを準備(お酒の量,タバコの量,生活習慣病かどうか(true=1,false=0))
input_data = np.array([[1,1,0],
                      [1,4,0],
                      [3,1,0],
                      [4,5,1],
                      [0,7,1]])

#初期設定
epochs=1000
alpha = 0.1
b0 = random.random()
b1 = random.random()
b2 = random.random()

#繰り返し更新する
for j in range(epochs):
    #dbを初期化
    db0 = 0
    db1 = 0
    db2 = 0
    
    #dataの数だけ繰り返し
    for i in input_data:
        #input_dataを変巣に対応させる
        X1 = i[0]
        X2 = i[1]
        y = i[2]
        
        #目的関数を定義
        Z = b0 + b1*X1 + b2*X2
        #シグモイド関数を定義
        Sig = 1 / (1 + np.exp(-Z))
        

        #傾きを計算
        if y==1:
            #生活習慣病の場合
            db0 += (1-Sig)
            db1 += (1-Sig)*X1
            db2 += (1-Sig)*X2
        else:    
            #健康な場合
            db0 += -Sig
            db1 += -Sig*X1
            db2 += -Sig*X2
    
    #重みを更新
    #尤度関数は上に凸なので、最大になるようにαを設定
    b0 += alpha*db0
    b1 += alpha*db1
    b2 += alpha*db2

#モデルの評価
#Zと0の大小で生活習慣かどうか決まる
'''
0=b0 + b1*x + b2*y
y=- (b0 + b1*x) / b2
'''
x=np.linspace(0,5,100)
y1=-(b0 + b1*x)/b2
#plt.plot(x,y1)
y2=1 / (1 + np.exp(-y1))
plt.plot(x,y2)

for k in input_data:
    plt.scatter(k[0],k[1])
