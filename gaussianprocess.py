from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import simps

filepath = "../ics_matterpow_0.dat"

data = np.loadtxt(filepath)
k_scale = data[:,0]
power = data[:,1]
logp = np.log10(power)

fig = plt.figure()
foo = plt.plot(k_scale,logp*k_scale**2)
plt.show()

def func(k,r):
    return power * k**2 * np.sin(k*r) / (k*r) / (2.*np.pi)

r_arr = np.linspace(1.,1000.,200)
xi = np.zeros(len(r_arr))
for i in range(len(r_arr)):
    r = r_arr[i]
    xi[i] = simps(func(k_scale,r),x=k_scale)

fig = plt.figure()
foo = plt.plot(np.log10(r_arr),r_arr**2*xi)
plt.show()


