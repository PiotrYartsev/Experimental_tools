#plot some thing in python
import matplotlib.pyplot as plt
import numpy
import math


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

frequancies_2=[5000,4500, 4000, 3500, 3000, 2500, 2000, 5500 , 6000, 6500, 7000, 7500, 8000]
offset_in_micro_meter=[0,-15.00, -31.40, -47.00 , -61.20, -82.40, -107.2, 11.50, 19.00, 22.00, 22.90, 22.90, 22.90]

#order a list from smallest to largest
def order_list(list_to_order):
    for n in range(len(list_to_order)):
        for m in range(len(list_to_order)-1):
            if list_to_order[m]>list_to_order[m+1]:
                list_to_order[m],list_to_order[m+1]=list_to_order[m+1],list_to_order[m]
    return list_to_order

order_list(frequancies_2)
order_list(offset_in_micro_meter)



error_in_offset_in_micro_meter=[0,0.2,0.2,0.2, 0.2, 0.4, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2]
print(len(frequancies_2))
print(len(offset_in_micro_meter))
print(len(error_in_offset_in_micro_meter))

#IN micro seconds 
R=1000
L=0.07958
C=1.2732*10**(-8)


x=numpy.linspace(2000,8000,1000)
H_abs=lambda w: ((R*C*w)/(math.sqrt((1-L*C*w**2)**2 + (R*C*w)**2)))
y_1=[]

for n in range(len(x)):
    y_1.append(H_abs(x[n]))
    print(y_1[n])

Angle_thing=lambda w: -math.atan((L*C*w**2-1)/(R*C*w))
#print(y_1)


y_2=[]
for n in range(len(x)):
    y_2.append(Angle_thing(x[n]))


plt.plot(frequancies,new_output_voltage)
plt.plot(x,y_1)

plt.xlabel('Frequencies')
plt.ylabel('Output Voltage')
plt.title('Output Voltage vs Frequencies')
plt.show()

#plt.plot(frequancies_2,offset_in_micro_meter)
plt.plot(x,y_2)
plt.xlabel('Frequencies')
plt.ylabel('Offset in micro meter')
plt.title('Offset in micro meter vs Frequencies')
plt.show()