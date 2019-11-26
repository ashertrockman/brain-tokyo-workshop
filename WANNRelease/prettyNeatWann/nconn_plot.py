import matplotlib.pyplot as plt


plt.rcParams["figure.figsize"] = (7, 5)


ncons = []
fits = []

with open('biped_cons.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        val = float(l.split(' ')[1].strip())
        if l.startswith('nConn'):
            ncons.append(val)
        else:
            fits.append(val)

avgs = {}

for i in range(0, len(ncons)):
    if ncons[i] not in avgs:
        avgs[ncons[i]] = [fits[i]]
    else:
        avgs[ncons[i]].append(fits[i])

ncons2 = []
fits2 = []

import numpy as np

for a in sorted(avgs.keys()):
    ncons2.append(a)
    fits2.append(np.mean(avgs[a]))

print(ncons2)
print(fits2)

plt.plot(ncons2, fits2, marker='o', markersize=4)
plt.xlabel('# Connections')
plt.ylabel('avg Max Fitness')
plt.title(r"$\bf{" + "Biped" + "}$ Fitness vs. # Connections")
plt.savefig('biped-ncons-fitness.png')
