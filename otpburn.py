import RPi.GPIO as GPIO
import time
from eegv5_prog_array import sr_fields_len, sr_fields

# --- Pin Definitions (Adjust these to your wiring) ---
CSB_PIN     = 19
SCLK_PIN    = 26
PGM_PIN     = 13
DIN_PIN     = 6
VDDQ_EN_PIN = 5

# --- GPIO Initialization ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(CSB_PIN,     GPIO.OUT)
GPIO.setup(SCLK_PIN,    GPIO.OUT)
GPIO.setup(PGM_PIN,     GPIO.OUT)
GPIO.setup(DIN_PIN,     GPIO.OUT)
GPIO.setup(VDDQ_EN_PIN, GPIO.OUT)

# --- SR_Update Equivalent ---
def sr_update(csb, sclk, pgm, din, vddq_en):
    GPIO.output(CSB_PIN,     csb)
    GPIO.output(SCLK_PIN,    sclk)
    GPIO.output(PGM_PIN,     pgm)
    GPIO.output(DIN_PIN,     din)
    GPIO.output(VDDQ_EN_PIN, vddq_en)

# --- SR_Burn Function ---
def sr_burn():
    # Initialize SR interface: pgm=1, sclk=0, csb=1 before raising vddq_en
    pgm     = 1
    sclk    = 0
    csb     = 1
    din     = 0
    vddq_en = 0
    sr_update(csb, sclk, pgm, din, vddq_en)

    vddq_en = 1
    time.sleep(0.002)   # 100000 delay
    sr_update(csb, sclk, pgm, din, vddq_en)

    # Delay then toggle csb low
    time.sleep(0.004)   # 200000 delay
    csb = 0
    sr_update(csb, sclk, pgm, din, vddq_en)

    # Wait then toggle pgm low
    time.sleep(0.0002)  # 10000 delay
    pgm = 0
    sr_update(csb, sclk, pgm, din, vddq_en)

    # --- Main Burn Loop (LSB-first, pgm carries the data bit) ---
    fcount = 0
    while fcount < 69:
        lcount = 0
        while lcount < sr_fields_len[fcount]:
            time.sleep(0.0006)  # 30000 delay
            pgm = (sr_fields[fcount] >> lcount) & 1
            sr_update(csb, sclk, pgm, din, vddq_en)

            time.sleep(0.0006)  # 30000 delay
            sclk = 1
            sr_update(csb, sclk, pgm, din, vddq_en)

            time.sleep(0.0006)  # 30000 delay
            pgm = 0
            sr_update(csb, sclk, pgm, din, vddq_en)

            time.sleep(0.0006)  # 30000 delay
            sclk = 0
            sr_update(csb, sclk, pgm, din, vddq_en)

            lcount += 1

        fcount += 1
        print(f"fcount {fcount} lcount {lcount}")

    # --- Final State ---
    time.sleep(0.0002)  # 10000 delay
    csb = 1
    sr_update(csb, sclk, pgm, din, vddq_en)

    time.sleep(0.0006)  # 30000 delay
    vddq_en = 0
    sr_update(csb, sclk, pgm, din, vddq_en)

    return True

# --- Main Execution ---
try:
    sr_burn()
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
