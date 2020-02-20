from bbb_pru_adc.capture import capture 
t=[]

with capture(clk_div=893,step_avg=0,channels=[0],auto_install=False,max_num=1,target_delay=9999999) as cap:
     for num_dropped, timestamps, values in cap:
        t.append(timestamps[0])
        print(timestamps)
        print(values)
