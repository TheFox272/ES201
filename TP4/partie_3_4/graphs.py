import matplotlib.pyplot as plt
import numpy as np

A7_size = np.array([1, 2, 4, 8, 16])
A15_size = np.array([2, 4, 8, 16, 32])

A7_total_area = np.array([0.8273675840000001, 0.83970714, 0.8302143000000001, 0.8445378000000001, 0.8512613000000001]) #, 0.8957180000000001])
A15_total_area = np.array([2.350587624, 2.34059136, 2.35392884, 2.3585554999999996, 2.3994894])

ax = plt.gca()
ax.set_xscale("log", base=2)

ax.set_ylim(0, 3)
ax.set_xlabel("L1 cache size (KiB)")
ax.set_ylabel("Total area (mm²)")

ax.plot(A7_size, A7_total_area, "o-")
ax.plot(A15_size, A15_total_area, "o-")
ax.legend(["A7", "A15"])




plt.figure(2)

# Données calculées pour Blowfish

A7_IPC = np.array([0.3783 , 0.3961, 0.4889 , 0.5000 , 0.5088 ])
A15_IPC = np.array([0.9392 , 0.8977 , 1.0758 , 1.1312 , 1.1918 ])

A7_efficiency = A7_IPC / A7_total_area
A15_efficiency = A15_IPC / A15_total_area


ax = plt.gca()
ax.set_xscale("log", base=2)

ax.set_ylim(0, .8)
ax.set_xlabel("L1 cache size (KiB)")
ax.set_ylabel("Efficiency (IPC/mm²)")

ax.plot(A7_size, A7_efficiency, "o-")
ax.plot(A15_size, A15_efficiency, "o-")

ax.legend(["A7", "A15"])


plt.show()