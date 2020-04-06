import pickle
import matplotlib.pyplot as plt 
import numpy as np
import os

def IQ(adc_raw):
    adc_shape=np.shape(adc_raw)
    adc_raw=adc_raw.reshape(adc_shape[0]*2,2)
    adc_raw=adc_raw-np.mean(adc_raw)

    if(((adc_raw[0]>0)==[True,True]).all()):
        I_Qmask=[1,1]
    elif(((adc_raw[0]>0)==[True,False]).all()):
        I_Qmask=[1,-1]
    elif(((adc_raw[0]>0)==[False,True]).all()):
        I_Qmask=[-1,1]
    else:
        I_Qmask=[-1,-1]

    I=[]
    Q=[]
    for i in range(len(adc_raw)):
        I.append(adc_raw[i][0]*I_Qmask[0])
        Q.append(adc_raw[i][1]*I_Qmask[1])
        I_Qmask=np.multiply(I_Qmask,-1)
    I=np.array(I)
    Q=np.array(Q)
    return [I,Q]
    phase_adc=np.arctan2(Q,I)
    phase_mo=np.arctan2(Q_MO,I_MO)
    deg=180*(phase_mo-phase_adc)/np.pi

    return deg

'''
script_dir = os.path.dirname(__file__)
rel_path = "2091/data.txt"
abs_file_path = os.path.join(script_dir, rel_path)
'''

with open('27_03_aqs/3_1.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_3=IQ[:,0]
Q_3=IQ[:,1]

with open('27_03_aqs/4_1.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_4=IQ[:,0]
Q_4=IQ[:,1]

with open('27_03_aqs/7_2.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_7=IQ[:,0]
Q_7=IQ[:,1]

with open('27_03_aqs/8_2.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_8=IQ[:,0]
Q_8=IQ[:,1]

with open('27_03_aqs/11_3.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_11=IQ[:,0]
Q_11=IQ[:,1]

with open('27_03_aqs/12_3.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_12=IQ[:,0]
Q_12=IQ[:,1]

with open('27_03_aqs/15_4.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_15=IQ[:,0]
Q_15=IQ[:,1]

with open('27_03_aqs/16_4.pickle','rb') as f:
    vars_f=pickle.load(f)
IQ=np.array(vars_f[1])
I_16=IQ[:,0]
Q_16=IQ[:,1]


max_len=np.min([len(I_3),len(I_7),len(I_11),len(I_15)])
max_len1=np.min([len(I_4),len(I_8),len(I_12),len(I_16)])

I_3=I_3[0:max_len]
I_7=I_7[0:max_len]
I_11=I_11[0:max_len]
I_15=I_15[0:max_len]

Q_3=Q_3[0:max_len]
Q_7=Q_7[0:max_len]
Q_11=Q_11[0:max_len]
Q_15=Q_15[0:max_len]

I_4=I_4[0:max_len1]
I_8=I_8[0:max_len1]
I_12=I_12[0:max_len1]
I_16=I_16[0:max_len1]

Q_4=Q_4[0:max_len1]
Q_8=Q_8[0:max_len1]
Q_12=Q_12[0:max_len1]
Q_16=Q_16[0:max_len1]
'''
plt.subplot(211)
plt.plot(I_4,label='IQ 4 samples')
plt.plot(I_8,label='IQ 8 samples')
plt.plot(I_12,label='IQ 12 samples')
plt.plot(I_16,label='IQ 16 samples')

plt.legend()

plt.subplot(212)
plt.plot(Q_4,label='IQ 4 samples')
plt.plot(Q_8,label='IQ 8 samples')
plt.plot(Q_12,label='IQ 12 samples')
plt.plot(Q_16,label='IQ 16 samples')
plt.legend()

plt.figure()

plt.subplot(211)
plt.plot(I_3,label='IQ 3 samples')
plt.plot(I_7,label='IQ 7 samples')
plt.plot(I_11,label='IQ 11 samples')
plt.plot(I_15,label='IQ 15 samples')

plt.legend()

plt.subplot(212)
plt.plot(Q_3,label='IQ 3 samples')
plt.plot(Q_7,label='IQ 7 samples')
plt.plot(Q_11,label='IQ 11 samples')
plt.plot(Q_15,label='IQ 15 samples')
plt.legend()
'''
SNRI4=20*np.log(np.std(I_4))
SNRI8=20*np.log(np.std(I_8))
SNRI12=20*np.log(np.std(I_12))
SNRI16=20*np.log(np.std(I_16))

SNRQ4=20*np.log(np.std(Q_4))
SNRQ8=20*np.log(np.std(Q_8))
SNRQ12=20*np.log(np.std(Q_12))
SNRQ16=20*np.log(np.std(Q_16))

SNRI3=20*np.log(np.std(I_3))
SNRI7=20*np.log(np.std(I_7))
SNRI11=20*np.log(np.std(I_11))
SNRI15=20*np.log(np.std(I_15))

SNRQ3=20*np.log(np.std(Q_3))
SNRQ7=20*np.log(np.std(Q_7))
SNRQ11=20*np.log(np.std(Q_11))
SNRQ15=20*np.log(np.std(Q_15))

print(SNRI4,SNRI8,SNRI12,SNRI16)
print(SNRQ4,SNRQ8,SNRQ12,SNRQ16)
print(SNRI3,SNRI7,SNRI11,SNRI15)
print(SNRQ3,SNRQ7,SNRQ11,SNRQ15)
'''
plt.show()