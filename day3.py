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
#Forward Propagation
Z1 = b11 + x1*w111 + x2*w121
Z2 = b12 + x1*w112 + x2*w122

O1 = Sig(Z1)
O2 = Sig(Z2)

Z = b21 + O1*w211 + O2*w221

Output = Sig(Z)

Error = (y - Output)**2

#differential
dw111 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x1
dw121 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))*x2
db11 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z1)*(1 - Sig(Z1))
dw112 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x1
dw122 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))*x2
db12 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*Sig(Z2)*(1 - Sig(Z2))
dw211 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O1
dw221 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))*O2
db21 = 2*(y - Output)*Sig(Z)*(1 - Sig(Z))

#Gradient Descent / Steepest Descent
w111 -= alpha(dw111)
w121 -= alpha(dw121)
b11 -= alpha(db11)
w112 -= alpha(dw112)
w122 -= alpha(dw122)
b12 -= alpha(db12)
w211 -= alpha(dw211)
w221 -= alpha(dw221)
b21 -= alpha(db21)



