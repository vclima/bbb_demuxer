import pickle
import matplotlib.pyplot as plt 
import numpy as np

with open('a.pickle','rb') as f:
    vars_f=pickle.load(f)

#t=np.linspace(10,200,num=4000)

spec=np.array(vars_f[2])
#ind=np.where(spec<0.05)[0][0]
#spec=spec[ind:ind+4000]
plt.plot(spec)

with open('b.pickle','rb') as f:
    vars_f=pickle.load(f)

#t=np.linspace(10,200,num=4000)

spec=np.array(vars_f[2])
#ind=np.where(spec<0.05)[0][0]
#spec=spec[ind:ind+4000]
plt.plot(spec)



with open('c.pickle','rb') as f:
    vars_f=pickle.load(f)

#t=np.linspace(10,200,num=4000)

spec=np.array(vars_f[2])
#ind=np.where(spec<0.05)[0][0]
#spec=spec[ind:ind+4000]
plt.plot(spec)
plt.show()
