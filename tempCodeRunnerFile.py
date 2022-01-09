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