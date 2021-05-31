import matplotlib.pyplot as plt
import numpy as np

num = np.arange(1000)

data = np.loadtxt("./data_evol_test3.txt")

W0_orig = data[0]
W1_orig = data[1]
W2_orig = data[2]
W0_evol = data[3]
W1_evol = data[4]
W2_evol = data[5]

evol_fig = plt.figure()            

plt.subplot(3,2,1)
plt.plot(num, W0_orig, 'o', color='red') 
plt.ylabel('density')
plt.title('Initial Condition')
plt.subplot(3,2,3)
plt.plot(num, W1_orig, 'o', color='green') 
plt.ylabel('velocity')
plt.subplot(3,2,5)
plt.plot(num, W2_orig, 'o', color='blue') 
plt.xlabel('position')
plt.ylabel('pressure')

plt.subplot(3,2,2)
plt.plot(num, W0_evol, 'o', color='red') 
plt.ylabel('density')
plt.title('Evolution')
plt.subplot(3,2,4)
plt.plot(num, W1_evol, 'o', color='green') 
plt.ylabel('velocity')
plt.subplot(3,2,6)
plt.plot(num, W2_evol, 'o', color='blue') 
plt.xlabel('position')
plt.ylabel('pressure')

plt.suptitle('Evolution of 1D Hydro tube')

plt.show()                   

