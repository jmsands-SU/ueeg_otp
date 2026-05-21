import RPi.GPIO as GPIO
import time
from eegv5_prog_array_adctest import sr_fields_len, sr_fields #<----This line needs to be uncommented, but requires the file
import threading
import logging

logging.basicConfig(
    filename='programming.log',
    format='%(asctime)s - %(message)s')
# --- Pin Definitions (Adjust these to your wiring) ---
CSB_PIN = 19
SCLK_PIN = 26
PGM_PIN = 13
DIN_PIN = 6
VDDQ_PIN = 5

# --- GPIO Initialization ---
GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbering
GPIO.setup(CSB_PIN, GPIO.OUT)
GPIO.setup(SCLK_PIN, GPIO.OUT)
GPIO.setup(PGM_PIN, GPIO.OUT)
GPIO.setup(DIN_PIN, GPIO.OUT)
GPIO.setup(VDDQ_PIN, GPIO.OUT)
# --- SR_Update Equivalent ---
def sr_update(csb, sclk, pgm, din, vddq):
    GPIO.output(CSB_PIN, csb)
    GPIO.output(SCLK_PIN, sclk)
    GPIO.output(PGM_PIN, pgm)
    GPIO.output(DIN_PIN, din)
    GPIO.output(VDDQ_PIN, vddq)

# --- SR_Write Function ---
def sr_write(csb_mode):
    # Initialize
    pgm = 0
    sclk = 1
    csb = csb_mode
    din = 0
    vddq = 0
    sr_update(csb, sclk, pgm, din, vddq)

    # Delay a bit then toggle csb low
    time.sleep(0.002)  # 1 millisecond delay
    csb = 0
    sr_update(csb, sclk, pgm, din, vddq)

    # ---  Main Data Transfer Loop  ---
    fcount = 69  # from original code
    # Replace this with your sr_fields_len and sr_fields
    #  These must be defined elsewhere and imported.  Example follows:
    # from eegv5_prog_array import sr_fields_len, sr_fields
    # if you have those arrays in a file eegv5_prog_array.py
    
    totalbits = 0
    lcount = 1
    errcount = 0

    while fcount > 0:
        fcount -= 1
        lcount = sr_fields_len[fcount]
        #print(f"fcount {fcount} lcount {lcount}")
        #print(sum(sr_fields_len))
        totalbits += lcount
        while lcount > 0:
            lcount -= 1
            din = (sr_fields[fcount] >> lcount) & 1
            #print(din)
            sr_update(csb, sclk, pgm, din, vddq)
            time.sleep(0.002) # Delay for SCLK_DELAY (adjust as needed)
            sclk = 0
            sr_update(csb, sclk, pgm, din, vddq)
            time.sleep(0.002) # Delay for SCLK_DELAY (adjust as needed)
            sclk = 1 # (fcount > 0) #Clock High
            if fcount == 0 and lcount == 0:
                sclk = 0
        #print(f"fcount {fcount} lcount {lcount}")

    # ---  Final State  ---
    csb = 0
    din = 0
    vddq = 0
    sr_update(csb, sclk, pgm, din, vddq)
    print(f"Number of errors found in readback: {errcount}")
    print(totalbits)
    return True

# --- Main Execution ---
try:
#     time.sleep(10)
#     # Example usage:  Enable chip select
#     combos_100k = { '100%':{'PWM_EN':0,'PA':1},
#                '50%':{'PWM_EN':1,'PA':8},
#                '25%':{'PWM_EN':1,'PA':4},
#                '12p5%':{'PWM_EN':1,'PA':2}
#         }
#     combos_400k = { '100%':{'PWM_EN':0,'PA':1},
#                '50%':{'PWM_EN':1,'PA':2},
#                '25%':{'PWM_EN':1,'PA':1}
#                     }
#     for clock in range(1,2):
#         print(time.time())
#         sr_fields[17] = [0b10000,0b00100][clock]
#         combos = [combos_100k,combos_400k][clock]
#         for power in [[6,1]]:#,[6,1]]:
#             sr_fields[16] = power[0]
#             #sr_fields[67] = power[1]
#             for i in combos:
#                 sr_fields[24] = combos[i]['PWM_EN']
#                 sr_fields[22] = combos[i]['PA']
#                 print(time.time())
#                 sr_write(1)   # csb_mode = 0: chip select active
#                 print(time.time())
#                 time.sleep(150)
#     print("hit stop now")
#     print("\a")
#     start_time = time.time()
#     params = []


    class ParameterScheduler:
        def __init__(self, parameter_sets, interval=60):
            self.parameter_sets = parameter_sets
            self.interval = interval
            self.current_index = 0
            self.timer = None
            
        def call_function(self):
            # Get current parameter set
            print(time.time(),self.current_index)
            logging.warning(self.current_index)
            if self.current_index > len(self.parameter_sets)-1:
                return
            params = self.parameter_sets[self.current_index]
            #Immediately start next timer because we don't want to include writing time
            if ((self.current_index + 1) != len(self.parameter_sets)):
                self.timer = threading.Timer(self.interval, self.call_function)
                self.timer.start()
            # Call the function
            sr_fields[8:11] = params[:3]
            sr_fields[41] = params[3]
            sr_fields[42] = params[3]
            sr_fields[43] = params[3]
            sr_fields[44] = params[3]
            sr_fields[45] = params[4]
            sr_fields[46] = params[4]
            sr_fields[47] = params[4]
            sr_fields[48] = params[4]
            sr_write(1)
            
                
            # Move to next parameter set
            self.current_index = (self.current_index + 1)
            

        
        def start(self):
            self.call_function()
        
        def stop(self):
            if self.timer:
                self.timer.cancel()
            
    low_vals = [250,260,270,270,292,315,339,363]#285,308,336,361,385]
    cm_vals = [273,285,309,332,356,380,403,427]
    high_vals = [278,302,326,350,374,397,421,445,468]
    #cm_vals = [273,298,322,348,372,400,425,451]
#     high_vals = [312,337,360,386,410,439,464,489,512]
    params = []
#     for vcm in range(1,8):
    for ampcurrent in [1,3,8]:
        for buffcurrent in [1,3,8]:
            for vcm,high,low in [[2,2,4],[3,3,5]]:
       
#                 for low in range(3,8):
#                     if cm_vals[vcm] < low_vals[low]:
#                         continue
#                     for high in range(1,9):
#                         if cm_vals[vcm] > high_vals[high]:
#                             continue
#                         if high_vals[high] -low_vals[low] > 75:
#                             continue
                params.append((vcm,high,low,ampcurrent,buffcurrent,cm_vals[vcm],high_vals[high],low_vals[low],high_vals[high]-low_vals[low]))
    params= params*2
    print(params)
    print(len(params),"params")
    logging.warning("start")
#     params = params[21:]
#     scheduler = ParameterScheduler(params, interval=480)
#     scheduler.start()
#     while scheduler.current_index <= len(params) -1:
#         print(scheduler.current_index,time.time())
#         time.sleep(35)
#     print(params[2])
#     sr_fields[8:11] = [3,3,5]#params[-1][:3]
#     
#     current = 1
#     sr_fields[41] = current
#     sr_fields[42] = current
#     sr_fields[43] = current
#     sr_fields[44] = current
#     sr_fields[45] = current
#     sr_fields[46] = current
#     sr_fields[47] = current
#     sr_fields[48] = current
#     print(sr_fields)
    sr_write(1)
#                 while True:       
#                     time.sleep(5)
                
#     sr_write(1)
except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
