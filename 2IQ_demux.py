import pickle
import numpy as np 
import matplotlib.pyplot as plt 


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

amp_adc=amp(I_adc,Q_adc)
ph_adc=phase(I_adc,Q_adc,I_mo,Q_mo)

plt.plot(amp_adc)
plt.show()
