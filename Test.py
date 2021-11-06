import matplotlib.pyplot as plt
import numpy as np

#oppgave 2 plot
plt.title('Aluminium filters of varying thickness. 60cm from radiation source for 30second ')
plt.ylabel('charge [nC]')
plt.xlabel('filter thickness [mm]')
x = np.array([0.50, 1.00, 1.50, 2.00, 3.00, 4.03, 5.03])
y = np.array([-7.28, -5.99, -5.09, -4.52, -3.62, -3.09, -2.66]) # Effectively y = x**2
plt.plot(x, y)
#e = np.array([0.07, 0.01, 0.01])
#gradient 
m, b = np.polyfit(x, y, 1)
#plt.plot(x, m*x + b)

#plt.errorbar(x, y, e, linestyle='None', marker='^')
print('nC=',m,'time +',b)
plt.show()
