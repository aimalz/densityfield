import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt




data = np.loadtxt('onerun.txt', delimiter=',')

data = data.T
redshifts = data[0]
rhos = (data[1]/np.mean(data[1]))-1.

sigma = .01

def kernel(X0, X):
    return np.exp(-((X0-X)**2)/(2*sigma**2))

#n = 50

#spacing = len(redshifts)/n

#smoothzs = [np.mean(redshifts[(spacing*x):(spacing*x)+spacing]) for x in range(0, n)]
#smoothrhos = [np.mean(rhos[(spacing*x):(spacing*x)+spacing]) for x in range(0, n)]
smoothrhos = np.zeros(len(rhos))
for i in range(0, len(rhos)):
    sum1 = 0
    sum2 = 0
    for j in range(0, len(rhos)):
        k = kernel(redshifts[i], redshifts[j]) #I know this is terrible, and slow, and I am very sorry
        sum1 += k*rhos[j]
        sum2 += k
    smoothrhos[i] = sum1/sum2
    print smoothrhos[i]

print smoothrhos

plt.plot(redshifts, rhos)
plt.plot(redshifts, smoothrhos)
plt.savefig('smoothing.png')
