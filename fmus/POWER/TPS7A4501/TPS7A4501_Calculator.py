# Configurable Values
from math import floor
from os import error

V_OUT = 2.5 # Voltage Output (Volts)


### DO NOT CHANGE CHANGE ###

# Note on resistance:
#   The datasheet specifies R1 must be below 4.17 kOhms
#   to minimze output voltage error. Thus a 4.0 kOhm resistor for
#   R1 can be assumed as the default.

R1 = 4000 # ohms

# IC Electrical Properties
V_IN_MIN = 1.21 #  Volts
V_IN_MAX = 20 # Volts
V_DROPOUT = .450 # Assuming worst case per datasheet (Volts)
I_ADJ_BIAS = .0003 # Adjustable Pin Current Bias (Amps)

# Recommended Passive Values As per Datasheet
IN_FILTER_CAP = 10 # microFarad
OUT_FILTER_CAP = 10 # microFarad

# Voltage Relationship equation in the datasheet is defined as:
# V_OUT = V_IN_MIN  * (1 + R2/R1) + I_ADJ * R2

R2 = (V_OUT - V_IN_MIN ) / (V_IN_MIN  * (1/R1) + I_ADJ_BIAS)
V_OUT_VERIFY = V_IN_MIN * (1 + R2/R1) + I_ADJ_BIAS * R2

R2 = floor(100 * R2)/100


# Check Errors in Calculation
if V_OUT_VERIFY > V_IN_MAX:
    error("Output Voltage Too High, must be under", V_IN_MAX)

if V_OUT_VERIFY  < V_IN_MIN:
    error("Output Voltage Too low, must be greater than ", V_IN_MIN)

# Prinout Final Values
print("Final Component Values for FMU - TPS7A4501:")
print(" ","Output Voltage:", V_OUT_VERIFY, "V")
print(" ","R1:", R1, "ohms", "|", "R2:", R2, "ohms")

print(" ","Input Capacitor:" , IN_FILTER_CAP, "uF")
print(" ","Output Capacitor:", OUT_FILTER_CAP, "uF")