from bbb_pru_adc.capture import capture 
import threading
import numpy as np


measure_lock=threading.Lock()

def ADC_read():

   global measure
   global read_delay
   global new_read
   global kill_thread

   Fs=20
   T=2

   measure=[0,0]

   clk=int(17000/Fs)
   clk_delay=int((1/(Fs*5e-9))-1)
   samples=int(Fs*T)

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


def main():

   global measure
   global read_delay
   global new_read
   global kill_thread
   global adc0
   global adc1
   global sample_time

   kill_thread=0
   new_read=0

   ADC_thread=threading.Thread(target=ADC_read)
   ADC_thread.start()
   adc0=[]
   adc1=[]
   sample_time=[]
   samples=0
   try:
      while(1):
         if(new_read):
            adc0.append(measure[0])
            adc1.append(measure[1])
            sample_time.extend(read_delay)
            measure_lock.acquire()
            new_read=0
            measure_lock.release()
            samples+=1
            print('Samples: ',samples)
   except KeyboardInterrupt:
      kill_thread=1
      print('Sending kill ADC thread signal')
      ADC_thread.join()

   print('ADC status is ',ADC_thread.isAlive())

   avg_sample=np.mean(sample_time[1:])*5e-9
   jitter=np.std(sample_time[1:])*5e-9

   print('Average sample time:',avg_sample)
   print('Average Jitter:',jitter)
   '''
   t=np.linspace(0,len(sample_time)*5e-9,len(sample_time))
   plt.plot(t,adc0,'r',t,adc1,'b')
   plt.title('ADC Readings')
   plt.show()
   '''

   

   
if __name__ == "__main__":
    main()