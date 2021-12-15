#plot some thing in python
import matplotlib.pyplot as plt

frequancies=[2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000]

input_voltage=20

output_voltage=[3.86,5.3,7.24,9.92,13.6,17.3,18.8,16.7,13.4,11,9.28,7.96,7.04]
error_output_voltage_sen_gånger_två=[3.88,5.32,7.28,9.96,13.7,17.4,18.9,16.8,13.5,11.2,9.32,8.08,7.08]
#worse result then first run, dont know why. Lost about 1 V in output_voltage


new_output_voltage=[]

for n in range(len(output_voltage)):
    new_output_voltage.append(output_voltage[n]/input_voltage)

leangth_of_one_period=[1969,2404,3012,3623,4049,4500,5000,5495,6061,6494,6897,7407,8000]
error_in_leangth_of_one_period=[1984,2427,2994,3597,4030,4484,4950,5464,5988,6452,6849,7353,7937]
start_offset_1=44 #micro meter
error_in_start_offset_1=2 #pm micro meter
start_offset_2_4000hz=10 #micro meter
error_in_start_offset_2_4000hz=1 #pm micro meter

plt.plot(frequancies,new_output_voltage)

plt.xlabel('Frequencies')
plt.ylabel('Output Voltage')
plt.title('Output Voltage vs Frequencies')
plt.show()