import pickle
import matplotlib.pyplot as plt 
import numpy as np 

with open('e.pickle','rb') as f:
    vars_f=pickle.load(f)

t=np.linspace(10,200,num=4000)

spec=np.array(vars_f[2])
ind=np.where(spec<0.05)[0][0]
spec=spec[ind:ind+4000]
plt.plot(t,spec)

with open('d.pickle','rb') as f:
    vars_f=pickle.load(f)

t=np.linspace(10,200,num=4000)

spec=np.array(vars_f[2])
ind=np.where(spec<0.05)[0][0]
spec=spec[ind:ind+4000]
plt.plot(t,spec)
plt.show()