import RPi.GPIO as GPIO
import time
from eegv4_prog import sr_fields_len, sr_fields #<----This line needs to be uncommented, but requires the file

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
    fcount = 62  # from original code
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
    #time.sleep(10)
    # Example usage:  Enable chip select
#     combos_100k = { '100%':{'PWM_EN':0,'PA':1},
#                '50%':{'PWM_EN':1,'PA':8},
#                '25%':{'PWM_EN':1,'PA':4},
#                '12p5%':{'PWM_EN':1,'PA':2}
#         }
#     combos_400k = { '100%':{'PWM_EN':0,'PA':1},
#                '50%':{'PWM_EN':1,'PA':2},
#                '25%':{'PWM_EN':1,'PA':1}
#                     }
#     for clock in range(2):
#         print(time.time())
#         sr_fields[17] = [0b10000,0b00100][clock]
#         combos = [combos_100k,combos_400k][clock]
#         for power in [[3,1],[7,0]]:
#             sr_fields[16] = power[0]
#             sr_fields[67] = power[1]
#             for i in combos:
#                 sr_fields[24] = combos[i]['PWM_EN']
#                 sr_fields[22] = combos[i]['PA']
#                 print(time.time())
#                 sr_write(1)   # csb_mode = 0: chip select active
#                 print(time.time())
#                 time.sleep(5)
#     print("hit stop now")
    sr_write(1)
except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit


