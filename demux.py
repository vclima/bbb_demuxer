from bbb_pru_adc.capture import capture 
import threading
import numpy as np


measure_lock=threading.Lock()

def ADC_read(m,n):

   global measure
   global read_delay
   global new_read
   global kill_thread

   F_sig=4
   Fs=F_sig*n/m
   

   measure=[0,0]

   clk=int(17000/Fs)
   clk_delay=int((1/(Fs*5e-9))-1)
   samples=n

   with capture(clk_div=clk,step_avg=0,channels=[0, 1],auto_install=False,max_num=samples,target_delay=clk_delay) as cap:
      for num_dropped, timestamps, values in cap:
         measure_lock.acquire()
         if(new_read):
            print('DROPPED READING')
         measure[0]=values[0::2]
         measure[1]=values[1::2]
         read_delay=timestamps[0:]
         new_read=1
         measure_lock.release()
         if(kill_thread):
            print('Finishing ADC execution')
            break
   
   print('Exiting ADC thread')

def IQ(m,n,adc_raw):
   j=np.arange(0,n)
   sin_vec=np.sin(j*2*np.pi*m/n)
   cos_vec=np.cos(j*2*np.pi*m/n)

   I=(2/n)*np.sum(np.multiply(cos_vec,adc_raw))
   Q=(2/n)*np.sum(np.multiply(sin_vec,adc_raw))

   return [I,Q]

def main():

   global measure
   global read_delay
   global new_read
   global kill_thread
   global adc0
   global MO
   global sample_time

   kill_thread=0
   new_read=0

   n=15
   m=4
   

   ADC_thread=threading.Thread(target=ADC_read,args=(m,n))
   ADC_thread.start()
   adc0=[]
   MO=[]
   sample_time=[]
   samples=0
   try:
      while(1):
         if(new_read):
            adc0.append(measure[0])
            MO.append(measure[1])
            sample_time.extend(read_delay)
            measure_lock.acquire()
            new_read=0
            measure_lock.release()
            samples+=1
            [I_MO,Q_MO]=IQ(m,n,MO)
            print('Samples: ',samples)
            print('I_MO:',I_MO,'Q_MO:',Q_MO)
   except KeyboardInterrupt:
      kill_thread=1
      print('Sending kill ADC thread signal')
      ADC_thread.join()

   print('ADC status is ',ADC_thread.isAlive())

   avg_sample=np.mean(sample_time[1:])*5e-9
   jitter=np.std(sample_time[1:])*5e-9

   print('Average sample time:',avg_sample)
   print('Average Jitter:',jitter)


   

   
if __name__ == "__main__":
    main()