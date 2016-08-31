from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import simps
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

filepath = "../ics_matterpow_0.dat"

data = np.loadtxt(filepath)
k_arr = data[:,0]
power = data[:,1]
logp = np.log10(power)
logk = np.log10(k_arr)

fig = plt.figure()
foo = plt.plot(logk,logp)
plt.xlabel(r"$\log k$")
plt.ylabel(r"$\log P(k)$")
plt.show()

fig = plt.figure()
foo = plt.plot(logk,logp*k_arr**2)
plt.xlabel(r"$\log k$")
plt.ylabel(r"$k^{2}\log P(k)$")
plt.show()

def p2cf(k,pk,r):
    return pk * k**2 * np.sin(k*r) / (k*r) / (2.*np.pi)

r_arr = np.linspace(1.,1000.,200)
xi = np.zeros(len(r_arr))
for i in range(len(r_arr)):
    r = r_arr[i]
    xi[i] = simps(p2cf(k_arr,power,r),x=k_arr)

fig = plt.figure()
foo = plt.plot(np.log10(r_arr),r_arr**2*xi)
plt.xlabel(r"$\log_{10}r$")
plt.ylabel(r"$r^{2} \xi(r)$")
plt.show()


