import pickle
import matplotlib.pyplot as plt 
import numpy as np


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

def amp(I,Q):
   amp=np.sqrt(I**2+Q**2)
   return amp

def phase(I,Q,I_MO,Q_MO):
   phase_adc=np.arctan2(Q,I)
   phase_mo=np.arctan2(Q_MO,I_MO)
   deg=180*(phase_mo-phase_adc)/np.pi

   return deg

with open('4_1.pickle','rb') as f:
    vars_f=pickle.load(f)

adc_raw=np.array(vars_f[4])
[I_adc,Q_adc]=IQ(adc_raw)

mo_raw=np.array(vars_f[5])
[I_mo,Q_mo]=IQ(mo_raw)

amp_IQ2=amp(I_adc,Q_adc)
ph_IQ2=phase(I_adc,Q_adc,I_mo,Q_mo)

with open('4_1.pickle','rb') as f:
    vars_f=pickle.load(f)

amp_IQ4=np.array(vars_f[2])
ph_IQ4=np.array(vars_f[3])

with open('8_2.pickle','rb') as f:
    vars_f=pickle.load(f)

amp_IQ8=np.array(vars_f[2])
ph_IQ8=np.array(vars_f[3])

with open('16_4.pickle','rb') as f:
    vars_f=pickle.load(f)

amp_IQ16=np.array(vars_f[2])
ph_IQ16=np.array(vars_f[3])

#max_len=np.min([len(amp_IQ2),len(amp_IQ4),len(amp_IQ8),len(amp_IQ16)])
max_len=np.min([len(amp_IQ4),len(amp_IQ8),len(amp_IQ16)])

ph_IQ4[(ph_IQ4<0)]=ph_IQ4[(ph_IQ4<0)]+360

#amp_IQ2=amp_IQ2[0:max_len]
amp_IQ4=amp_IQ4[0:max_len]
amp_IQ8=amp_IQ8[0:max_len]
amp_IQ16=amp_IQ16[0:max_len]

#ph_IQ2=ph_IQ2[0:max_len]
ph_IQ4=ph_IQ4[0:max_len]
ph_IQ8=ph_IQ8[0:max_len]
ph_IQ16=ph_IQ16[0:max_len]


plt.subplot(211)
#plt.plot(amp_IQ2,label='IQ 2 samples')
plt.plot(amp_IQ4,label='IQ 3 samples')
plt.plot(amp_IQ8,label='IQ 7 samples')
plt.plot(amp_IQ16,label='IQ 15 samples')
plt.legend()

plt.subplot(212)
#plt.plot(ph_IQ2)
plt.plot(ph_IQ4)
plt.plot(ph_IQ8)
plt.plot(ph_IQ16)


#SNR2=20*np.log(np.mean(amp_IQ2)/np.std(amp_IQ2))
SNR4=20*np.log(np.mean(amp_IQ4)/np.std(amp_IQ4))
SNR8=20*np.log(np.mean(amp_IQ8)/np.std(amp_IQ8))
SNR16=20*np.log(np.mean(amp_IQ16)/np.std(amp_IQ16))

#print(SNR2,SNR4,SNR8,SNR16)
print(SNR4,SNR8,SNR16)

plt.show()