from bbb_pru_adc.capture import capture 
import threading

measure_lock=threading.Lock()

def ADC_read():

   global measure
   global read_delay
   global new_read
   global kill_thread

   with capture(clk_div=8934,step_avg=0,channels=[1],auto_install=False,max_num=1,target_delay=99999999) as cap:
      for num_dropped, timestamps, values in cap:
         measure_lock.acquire()
         if(new_read):
            print('DROPPED READING')
         measure=values[0]
         read_delay=timestamps[0]
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

   kill_thread=0
   new_read=0

   ADC_thread=threading.Thread(target=ADC_read)
   ADC_thread.start()
   
   try:
      while(1):
         if(new_read):
            print(measure)
            print(read_delay)
            measure_lock.acquire()
            new_read=0
            measure_lock.release()
   except:
      kill_thread=1
      print('Sending kill ADC thread signal')
      ADC_thread.join()

   print('ADC status is ',ADC_thread.isAlive())

   

   
if __name__ == "__main__":
    main()