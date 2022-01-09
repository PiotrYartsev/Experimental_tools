#Measuring the shmit trigger
import matplotlib.lines as lines
import matplotlib.patches as mpatches

voltage_in=[-1.287,-0.826, 0.112,0.340,0.560,0.736, 0.879, -0.043, -0.250, -0.329 , -0.361, -0.467, -0.577, -0.748, -0.816, -0.848, -0.940, -1.022, -2.015, 0.611, 0.736, 0.711, -0.778, -0.812, -0.949, -1.085 , -1.212, 0.719, 0.793, 0.801, 0.825, 0.859, 0.906, 0.891, 2.029, -0.902, -0.970, -0.965, -1.007, -1.126, -1.116]

voltage_out=[-7.92,-7.92,-7.92,-7.92,-7.92, -7.92, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, -7.92, -7.92, -7.92, -7.92, 10.01, 10.01, 10.01, 10.01, -7.92, -7.92, -7.92, 10.01, -7.92, -7.92, -7.92, -7.92, 10.01, 10.01, 10.01, 10.01, 10.02, 10.02, -7.92, -7.92] 

R_1=1 #kohm

R_2=9 #kohm

V_1=10.07 #Volt
V_2=-10.03 #Volt

#plot the stuff
from matplotlib import lines
import matplotlib.pyplot as plt
from numpy.lib.twodim_base import triu_indices_from
print("The leangth of volage_in is:",len(voltage_in))
print("The leangth of voltage_out is:",len(voltage_out))

print(" \nThe turn points are:")
turn_points_x=[]
turn_points_y=[]

for n in range(len(voltage_in)):
    if n+1<len(voltage_in):
        if (voltage_out[n]<voltage_out[n+1]):
            if voltage_in[n]>0:
                print(voltage_in[n])
                turn_points_x.append(voltage_in[n])
                turn_points_y.append(voltage_out[n])
        if (voltage_out[n]>voltage_out[n+1]):
            if voltage_in[n]<0:
                print(voltage_in[n])
                turn_points_x.append(voltage_in[n])
                turn_points_y.append(voltage_out[n])


for k in range(len(turn_points_x)):
    inte1=0
    if turn_points_x[k]<turn_points_x[inte1]:
        inte1=k
for k in range(len(turn_points_x)):
    inte2=0
    if turn_points_x[k]>turn_points_x[inte2]:
        inte2=k
first_turn_point_x=[turn_points_x[inte1],turn_points_x[inte2]]
first_turn_points_y=[turn_points_y[inte1],turn_points_y[inte2]]

print("asdada",first_turn_point_x)
turn_a=((R_1)/(R_2*R_1))*V_1
turn_b=((R_1)/(R_2*R_1))*V_2

print(" \nThe turn points are:" ,turn_a)
print(" \nThe turn points are:" ,turn_b)

turn_points_x_2=[]
turn_points_y_2=[]


plt.plot(turn_points_x,turn_points_y, 'ro')
plt.plot(voltage_in,voltage_out,'b.')
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Output Voltage vs Input Voltage')
#plt.vlines(turn_a, V_2, V_1, colors='black', linestyles='dashed')
plt.vlines(turn_b, V_2, V_1, colors='black', linestyles='dashed')
plt.hlines(V_2,min(voltage_in) , turn_a, colors='black', linestyles='dashed')
plt.hlines(V_1,max(voltage_in) , turn_b, colors='black', linestyles='dashed')
plt.plot([turn_a,turn_a],[V_1,V_2], color='black', linestyle='dashed')
plt.axhline(0,color='black',linewidth=0.5) # x = 0
plt.axvline(0,color='black',linewidth=0.5) # y = 0
plt.legend(['Trigger points','Measured values',"Therory: "r"$V_{fm}=\frac{R_1}{R_1 + R_2} V_{ut, m}, V_{fM}=\frac{R_1}{R_1 + R_2} V_{ut, M}$"],)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()

list1=[]
list2=[]
list3=[]
list4=[]

for n in range(len(voltage_in)):
    if voltage_in[n]<0:
        #print(voltage_in[n], '&',  voltage_out[n], '\\\ \hline')
        list1.append(voltage_in[n])
        list2.append(voltage_out[n])
    
print("\n  \n")
for n in range(len(voltage_in)):
    if voltage_in[n]>0:
        #print(voltage_in[n], '&',  voltage_out[n], '\\\ \hline')
        list3.append(voltage_in[n])
        list4.append(voltage_out[n])
for o in range(len(list1)):
    print(list1[o], '&',  list2[o], '&', list3[o],'&',list4[o], '\\\ \hline')
