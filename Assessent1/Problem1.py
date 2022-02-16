import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

array = np.loadtxt('lisbon_temp_fmt.txt')
print("Size of Data elements",array.size)
print("Size of Data elements",array.shape)


plt.plot(array)

#clear nans and chnage it's values to interpolation values

nans= np.isnan(array)

for i in range(nans.size):
	if nans[i]!=False :
		#array[i]=0
		f=interp1d([i-3.,i-2.,i-1.], [array[i-3],array[i-2],array[i-1]], fill_value='extrapolate')
		array[i]= f(i)

plt.plot(array)


#clear outliers
for i in range(array.size):
	if abs(np.mean(array)-array[i])>3*np.std(array):
		print('!')
		if np.mean(array)>array[i]:
			array[i] = np.mean(array)-2.5*np.std(array)
			print('!')
		else:
			 array[i]= np.mean(array)+2.5*np.std(array)
plt.plot(array)



print(f'mean: {np.mean(array)}')
print(f'std: {np.std(array)}')

plt.show()



