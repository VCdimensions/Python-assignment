# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:34:50 2016

@author: SUNG ANN LEE
"""

import numpy as np
import matplotlib.pyplot as plt

Interval = 500
ST = np.arange(K - Interval,K + Interval)

###Buy Call & Sell Call
K_Call = 9000
Premium_Call = 140
Payoff_LongCall = np.maximum(ST-K,0) - Premium_Call
Payoff_ShortCall = Premium_Call - np.maximum(ST-K,0)

plt.plot(ST,Payoff_LongCall,linewidth=4,color='r',label='Long Call')
plt.plot(ST,Payoff_ShortCall,linewidth=4,color='b',label='Short Call')
plt.axhline(linewidth=1, color='black')
plt.legend(loc=2)
plt.show()

###Buy Put & Sell Put
K_Put = 9000
Premium_Put = 50

Payoff_LongPut = np.maximum(K-ST,0) - Premium_Put
Payoff_ShortPut = Premium_Put - np.maximum(K-ST,0)

plt.plot(ST,Payoff_LongPut,linewidth=4,color='r',label='Long Call')
plt.plot(ST,Payoff_ShortPut,linewidth=4,color='b',label='Short Call')
plt.axhline(linewidth=1, color='black')
plt.legend(loc=1)
plt.show()

###Butterfly Spread
K_Call1 = 9000
K_Call2 = 9100
K_Call3 = 9200

Premium_Call1 = 200
Premium_Call2 = 120
Premium_Call3 = 100

Payoff_Call1 = np.maximum(ST-K_Call1,0) - Premium_Call1
Payoff_Call2 = np.maximum(ST-K_Call2,0) - Premium_Call2
Payoff_Call3 = np.maximum(ST-K_Call3,0) - Premium_Call3

Butterfly = Payoff_Call1 - (2*Payoff_Call2) + Payoff_Call3

plt.plot(ST,Payoff_Call1,'-.',linewidth=2,color='#FF0000',label='Long 1 Call1')
plt.plot(ST,-2*Payoff_Call2,'-.',linewidth=2,color='#00FF00',label='Short 2 Call2')
plt.plot(ST,Payoff_Call3,'-.',linewidth=2,color='#0000FF',label='Long 1 Call3')
plt.plot(ST,Butterfly,color="black",linewidth=4,label='Butterfly Spread')
plt.axhline(linewidth=1, color='#445400')
plt.legend(loc=3)
plt.show()


