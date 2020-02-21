from bbb_pru_adc.capture import capture 
import threading

measure_lock=threading.Lock()

def ADC_read():

   global measure
   global read_delay
   global new_read

   with capture(clk_div=893,step_avg=0,channels=[0],auto_install=False,max_num=1,target_delay=9999999) as cap:
      for num_dropped, timestamps, values in cap:
         measure_lock.acquire()
         if(new_read):
            print('DROPPED READING')
         measure=values[0]
         read_delay=timestamps[0]
         new_read=1
         measure_lock.release()

def main():

   global measure
   global read_delay
   global new_read

   ADC_daemon=threading.Thread(target=ADC_read)
   ADC_daemon.daemon=True
   ADC_daemon.start()
   
   while(1):
      if(new_read):
         print(measure)
         print(read_delay)
         measure_lock.acquire()
         new_read=0
         measure_lock.release()

if __name__ == "__main__":
    main()