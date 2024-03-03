import matplotlib.pyplot as plt
import numpy as np


# L1 cache size vs. Area proc + 2 L1 + L2 

plt.figure(1)

A7_size = np.array([1, 2, 4, 8, 16])
A15_size = np.array([2, 4, 8, 16, 32])

A7_total_area = np.array([0.8273675840000001, 0.83970714, 0.8302143000000001, 0.8445378000000001, 0.8512613000000001]) #, 0.8957180000000001])
A15_total_area = np.array([2.350587624, 2.34059136, 2.35392884, 2.3585554999999996, 2.3994894])

ax = plt.gca()
ax.set_xscale("log", base=2)

ax.set_ylim(0, 3)
ax.set_xlabel("L1 cache size (KiB)")
ax.set_ylabel("Total area (mm²)")

ax.plot(A7_size, A7_total_area, "o-", color='#1f77b4')
ax.plot(A15_size, A15_total_area, "o-", color='#2ca02c')
ax.legend(["A7", "A15"])
ax.set_title("Area")



# L1 cache size vs. Efficacité surfacique avec L2
# Dijkstra et Blowfish

plt.figure(2)

A7_IPC_dijkstra = np.array([0.3783 , 0.3961, 0.4889 , 0.5000 , 0.5088 ])
A7_IPC_blowfish = np.array([0.3649 , 0.3928 , 0.4195 , 0.4803 , 0.4894 ])

A15_IPC_dijkstra = np.array([0.9392 , 0.8977 , 1.0758 , 1.1312 , 1.1918 ])
A15_IPC_blowfish = np.array([0.9321 , 1.2941 , 1.3239 , 1.3633 , 2.0729 ])

A7_area_efficiency_dijkstra = A7_IPC_dijkstra / A7_total_area
A7_area_efficiency_blowfish = A7_IPC_blowfish / A7_total_area

A15_area_efficiency_dijkstra = A15_IPC_dijkstra / A15_total_area
A15_area_efficiency_blowfish = A15_IPC_blowfish / A15_total_area


ax = plt.gca()
ax.set_xscale("log", base=2)

ax.set_ylim(0, 1)
ax.set_xlabel("L1 cache size (KiB)")
ax.set_ylabel("Efficiency (IPC/mm²)")

ax.plot(A7_size, A7_area_efficiency_dijkstra, "o-")
ax.plot(A7_size, A7_area_efficiency_blowfish, "o-")

ax.plot(A15_size, A15_area_efficiency_dijkstra, "o-")
ax.plot(A15_size, A15_area_efficiency_blowfish, "o-")

ax.legend(["A7 dijkstra", "A7 blowfish", "A15 dijkstra", "A15 blowfish"])
ax.set_title("Area Efficiency")



# L1 cache size vs. Efficacité énergétique hors L2

plt.figure(3)
# A7_power = np.array( [429.5158138326633, 438.290650317782, 439.7005726427026, 444.79356573677114, 462.54843489878095]) #, 504.9631522516877])
# A15_power = np.array([832.8616820299354, 833.726046018594, 835.0970092875704, 856.5908113613577, 891.8253953687693])

p_rw_dijkstra = .344
p_rw_blowfish = .2548

A7_L1_power = np.array([9.064081144350169, 13.451499386909527, 14.156460549369815, 16.70295709640407, 25.580391677408983]) #, 46.78775035386236]
A15_L1_power = np.array([13.567975081504306, 14.000157075833627, 14.68563871032174, 25.43253974721548, 43.049831750921236])


A7_power_dijkstra = 100 + 2 * A7_L1_power * p_rw_dijkstra
A7_power_blowfish = 100 + 2 * A7_L1_power * p_rw_blowfish
A15_power_dijkstra = 500 + 2 * A15_L1_power * p_rw_dijkstra
A15_power_blowfish = 500 + 2 * A15_L1_power * p_rw_blowfish

A7_energy_efficiency_dijkstra = A7_IPC_dijkstra / A7_power_dijkstra
A7_energy_efficiency_blowfish = A7_IPC_blowfish / A7_power_blowfish

A15_energy_efficiency_dijkstra = A15_IPC_dijkstra / A15_power_dijkstra
A15_energy_efficiency_blowfish = A15_IPC_blowfish / A15_power_blowfish


ax = plt.gca()
ax.plot(A7_size, A7_energy_efficiency_dijkstra, "o-")
ax.plot(A7_size, A7_energy_efficiency_blowfish, "o-")
ax.plot(A15_size, A15_energy_efficiency_dijkstra, "o-")
ax.plot(A15_size, A15_energy_efficiency_blowfish, "o-")

ax.set_xscale("log", base=2)

ax.set_ylim(0, .0050)
ax.set_xlabel("L1 cache size (KiB)")
ax.set_ylabel("Efficiency (IPC/mW)")

ax.legend(["A7 dijkstra", "A7 blowfish", "A15 dijkstra", "A15 blowfish"])
ax.set_title("Energy Efficiency (without L2)")

plt.show()





