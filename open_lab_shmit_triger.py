#Measuring the shmit trigger

voltage_in=[-1.287,-0.826, 0.112,0.340,0.560,0.736, 0.879, -0.043, -0.250, -0.329 , -0.361, -0.467, -0.577, -0.748, -0.816, -0.848, -0.940, -1.022, -2.015,]

voltage_out=[-7.92,-7.92,-7.92,-7.92,-7.92, -7.92, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, 10.01, -7.92, -7.92]

R_1=1 #kohm

R_2=9 #kohm

V_1=10.07 #Volt
V_2=10.03 #Volt

#plot the stuff
import matplotlib.pyplot as plt

plt.plot(voltage_in,voltage_out)
plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Output Voltage vs Input Voltage')
plt.show()