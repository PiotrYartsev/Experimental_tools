#plot output current vs input current

from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt

offset=0.03 #Volt

voltage_over_chip=10.00 #Volt
error_in_voltage_over_chip=0.01 #Volt

voltage_into_potentiometer=5.00 #Volt
error_in_voltage_into_potentiometer=0.01 #Volt


#for 1x multiplier we use a wire as R_2 and a 2kohm resistor as R_1


#for a 5x multiplier we use R_2 2+2+2+2=8kohm and R_1 2kohm


#for a 10x multiplier we use R_2 9 kohm (using a resistor board) and R_1 1kohm

voltage_into=[0.00,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00,1.10,1.20,1.30,1.40]
voltage_ampligied=[0.02,0.98,2.00,2.92,3.87,4.82,5.74,6.71,7.58,7.83,7.83,7.83,7.83,7.83,7.83]


A_omega=1+9000/1000


Asymptotic_function= lambda x: A_omega*x

Asymptotic_function_list=[]
for volt in voltage_into:
    Asymptotic_function_list.append(Asymptotic_function(volt))



plt.plot(voltage_into,Asymptotic_function_list, 'r', linestyle=':')
plt.plot(voltage_into,voltage_ampligied, 'b.')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Output Voltage vs Input Voltage')
plt.legend([r"$V_{\mathrm{OUT}}=V_{IN} \cdot A_{\infty}$",'Measured value'])
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.ylim(0)
plt.xlim(0, 1.4)
plt.show()