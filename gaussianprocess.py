from __future__ import print_function
import numpy as np
from math import pow
from matplotlib import pyplot as plt
from scipy.integrate import simps
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

filepath = "../ics_matterpow_0.dat"

# read data with k and power spectrum
data = np.loadtxt(filepath)
k_arr = data[:,0]
pspec = data[:,1]
logp = np.log10(pspec)
logk = np.log10(k_arr)

# plot power spectrum
plt.figure(figsize=(13,5))
ax1 = plt.subplot(1,2,1)
foo = plt.plot(logk,logp)
plt.xlabel(r"$\log k$")
plt.ylabel(r"$\log P(k)$")
ax2 = plt.subplot(1,2,2)
foo = plt.plot(logk,logp*k_arr**2)
plt.xlabel(r"$\log k$")
plt.ylabel(r"$k^{2}\log P(k)$")
plt.show()

# define useful functions for calculating correlation function

def func(k,pk,r):
    # k and pk must be matched arrays
    # r is scalar
    return k**2 * pk * np.sin(k*r) / (k*r) / (2.*np.pi**2)

def P2cf(Pk,k_arr,r_arr):
    xi = np.zeros(len(r_arr))
    for i in range(len(r_arr)):
        r = r_arr[i]
        xi[i] = simps(func(k_arr,Pk,r),x=k_arr)
    return xi


# First try defining separation array in log-space
logr_arr = np.linspace(0.,2.5,100)
r_arr = np.power(10.,logr_arr)
xi = P2cf(pspec,k_arr,r_arr)

plt.figure(figsize=(13,5))
ax1 = plt.subplot(1,2,1)
foo = plt.plot(np.log10(r_arr),xi)
plt.xlabel(r"$\log_{10}r$")
plt.ylabel(r"$\xi(r)$")
ax2 = plt.subplot(1,2,2)
foo = plt.plot(np.log10(r_arr),xi*r_arr**2)
plt.xlabel(r"$\log_{10}r$")
plt.ylabel(r"$r^{2}\xi(r)$")
#foo = plt.plot(np.log10(r_arr),np.log10(xi))
#plt.xlabel(r"$\log_{10}r$")
#plt.ylabel(r"$\log_{10}\xi(r)$")
plt.show()


# THen try defining separation array in linear-space
r_arr = np.linspace(1.,200.,200)
xi = P2cf(pspec,k_arr,r_arr)

plt.figure(figsize=(14,5))
ax1 = plt.subplot(1,2,1)
foo = plt.plot(np.log10(r_arr),xi)
plt.xlabel(r"$\log_{10}r$")
plt.ylabel(r"$\xi(r)$")
ax2 = plt.subplot(1,2,2)
foo = plt.plot(np.log10(r_arr),xi*r_arr**2)
plt.xlabel(r"$\log_{10}r$")
plt.ylabel(r"$r^{2}\xi(r)$")
#foo = plt.plot(np.log10(r_arr),np.log10(xi))
#plt.xlabel(r"$\log_{10}r$")
#plt.ylabel(r"$\log_{10}\xi(r)$")
plt.show()


