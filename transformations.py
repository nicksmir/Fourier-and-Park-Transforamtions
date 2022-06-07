import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.fftpack import dct
import pandas as pd
import xlrd
import openpyxl
import math
from numpy import array, arange, abs as np_abs
from numpy.fft import rfft, rfftfreq
from numpy.random import uniform
from math import sin, pi
import matplotlib.pyplot as plt

# Getting results of data capture from Excel
rslt = pd.read_excel('C:/Users/.../book1.xlsx',sheet_name='Time-Domain', usecols=['Ua','Ub','Uc','Ud','Uq','Ia','Ib', 'Ic','Id','Iq'])
rslt2 = pd.read_excel('C:/Users/.../book1.xlsx', sheet_name='Frequency-Domain', usecols=['Ua','Ub','Uc','Ia','Ib','Ic', 'U_Park','I_Park'])
# Data lists from Time-Domain
list1=list(rslt['Ua'])
# print(list1)
list2=list(rslt['Ub'])
# print(list2)
list3=list(rslt['Uc'])
# print(list3)
list6=list(rslt['Ia'])
# print(list6)
list7=list(rslt['Ib'])
# print(list7)
list8=list(rslt['Ic'])
# print(list8)
# Data lists from Time-Frequency
list11=list(rslt2['Ua'])
# print(list11)
list12=list(rslt2['Ub'])
# print(list12)
list13=list(rslt2['Uc'])
# print(list13)
list14=list(rslt2['Ia'])
# print(list14)
list15=list(rslt2['Ib'])
# print(list15)
list16=list(rslt2['Ic'])
# print(list16)

# #  Godograph Voltage
# Ud=[0]*len(list1)
# Uq=[0]*len(list2)
# for i in range(len(list1)):
#     Uq[i] = (list1[i]*0.8+list2[i]*(-0.4)+list3[i]*(-0.4))
#     Ud[i] = 0.5*(list2[i]-list3[i])
# plt.plot(Uq,Ud)
# plt.grid()
# plt.xlabel("d")
# plt.ylabel("q")
# plt.title("Voltage")
# plt.show()

# # Fourier Voltage
# Ua=fft(list1)
# Ub=fft(list2)
# Uc=fft(list3)
# fig,ax= plt.subplots()
# x = np.arange(0,20000,0.1)
# plt.plot(x,Ua)
# plt.plot(x,Ub)
# plt.plot(x,Uc)
# plt.show()

# Fourier Voltage
# Ia=fft(list6)
# Ib=fft(list7)
# Ic=fft(list8)
# fig,ax= plt.subplots()
# x = np.arange(0,20000,0.1)
# plt.plot(x,Ia)
# plt.plot(x,Ib)
# plt.plot(x,Ic)
# plt.show()

# # Park_U
# a=(math.sqrt(3))/2
# Ud=[0]*len(list11)
# Uq=[0]*len(list12)
# PU=[0]*len(list11)
# tetau=[0]*len(list11)
# for i in range(len(list11)):
#     if (math.sqrt(3)*abs(list11[i]))==0:
#        tetau[i]=0
#     else: tetau[i]=math.atan((list12[i]-list13[i])/(math.sqrt(3)*(list11[i])))
#     Uq[i] = a * (list11[i]*math.cos(tetau[i])+list12[i]*math.cos(tetau[i]-2*math.pi/3)+list13[i]*math.cos(tetau[i]+2*math.pi/3))
#     Ud[i] = 0.5 * (list11[i]*math.sin(tetau[i])+list12[i]*math.sin(tetau[i]-2*math.pi/3)+list13[i]*math.sin(tetau[i]+2*math.pi/3))
#     PU[i]=-100+math.fabs(Ud[i]+Uq[i])
# plt.plot(PU)
# plt.show()

# # Park_I
# a=(math.sqrt(3))/2
# Id=[0]*len(list14)
# Iq=[0]*len(list15)
# PI=[0]*len(list16)
# tetau=[0]*len(list14)
# for i in range(len(list14)):
#     if (math.sqrt(3)*abs(list14[i]))==0:
#        tetau[i]=0
#     else: tetau[i]=math.atan((list15[i]-list16[i])/(math.sqrt(3)*(list14[i])))
#     Iq[i] = a * (list14[i]*math.cos(tetau[i])+list15[i]*math.cos(tetau[i]-2*math.pi/3)+list16[i]*math.cos(tetau[i]+2*math.pi/3))
#     Id[i] = 0.5 * (list14[i]*math.sin(tetau[i])+list15[i]*math.sin(tetau[i]-2*math.pi/3)+list16[i]*math.sin(tetau[i]+2*math.pi/3))
#     PI[i]=-100+math.fabs(Id[i]+Iq[i])
# plt.plot(PI)
# plt.show()

# #  Godograph Voltage
Ud=[0]*len(list11)
Uq=[0]*len(list12)
PU=[0]*len(list11)
for i in range(len(list11)):
    Uq[i] = (list11[i]*0.8+list12[i]*(-0.4)+list13[i]*(-0.4))
    Ud[i] = 0.5*(list12[i]-list13[i])
    Uq[i] = math.fabs(Uq[i])
plt.plot(Uq)
plt.show()
