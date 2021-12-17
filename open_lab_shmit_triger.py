#Measuring the shmit trigger

voltage_in=[-1.287,-0.826, 0.112,0.340,0.560,0.736, 0.879, -0.043, -0.250, -0.329 , -0.361, -0.467, -0.577, -0.748, -0.816, -0.848, -0.940, -1.022, -2.015, 0.611, 0.736, 0.711, -0.778, -0.812, -0.949, -1.085 , -1.212, 0.719, 0.793, 0.801, 0.825, 0.859, 0.906, 0.891, 2.029, -0.902, -0.970, -1.116, -0.965, -1.007, -1.126]

voltage_out=[-7.92,-7.92,-7.92,-7.92,-7.92, -7.92, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, -7.92, -7.92, -7.92, -7.92, 10.01, 10.01, 10.01, 10.01, -7.92, -7.92, -7.92, 10.01, -7.92, -7.29, -7.92, -7.92, 10.01, 10.01, 10.01, 10.01, -7.93, 10.02, 10.02, -7.93] 

R_1=1 #kohm

R_2=9 #kohm

V_1=10.07 #Volt
V_2=10.03 #Volt

#plot the stuff
import matplotlib.pyplot as plt
print("The leangth of volage_in is:",len(voltage_in))
print("The leangth of voltage_out is:",len(voltage_out))

print(" \nThe turn points are:")
for n in range(len(voltage_in)):
    if (voltage_out[n]-voltage_out[n-1])!=0:
        print(voltage_in[n])


plt.plot(voltage_in,voltage_out)
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Output Voltage vs Input Voltage')
plt.show()