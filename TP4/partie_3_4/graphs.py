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



# L1 cache size vs. Efficacité énergétique

plt.figure(3)

p_rw_dijkstra = .344
p_rw_blowfish = .2548

A7_L1_power = np.array([9.064081144350169, 13.451499386909527, 14.156460549369815, 16.70295709640407, 25.580391677408983]) #, 46.78775035386236]
A15_L1_power = np.array([13.567975081504306, 14.000157075833627, 14.68563871032174, 25.43253974721548, 43.049831750921236])

A7_proc_power = 100
A15_proc_power = 500

A7_L2_power = 311.4
A15_L2_power = 305.7

# Miss rates

miss_A_7_IL1_dijkstra = np.array([0.2142, 0.2129, 0.0508, 0.0477, 0.0413])
miss_A_7_DL1_dijkstra = np.array([0.3727, 0.228, 0.1491, 0.1168, 0.0991])
# miss_A_7_L2_dijkstra  [0.0001, 0.0001, 0.0003, 0.0003, 0.0004]
miss_A_7_IL1_blowfish = np.array([0.2396, 0.217, 0.1883, 0.1179, 0.1171])
miss_A_7_DL1_blowfish = np.array([0.6141, 0.4244, 0.3243, 0.2879, 0.2446])
# miss_A_7_L2_blowfish  [0.0009, 0.001, 0.0012, 0.002, 0.002]
miss_A_15_IL1_dijkstra = np.array([0.0754, 0.072, 0.0186, 0.0148, 0.0107])
miss_A_15_DL1_dijkstra = np.array([0.1359, 0.0897, 0.0659, 0.0433, 0.0195])
# miss_A_15_L2_dijkstra  [0.0001, 0.0001, 0.0003, 0.0004, 0.0006]
miss_A_15_IL1_blowfish = np.array([0.1029, 0.0595, 0.059, 0.056, 0.0085])
miss_A_15_DL1_blowfish = np.array([0.4018, 0.3217, 0.2489, 0.174, 0.033])
# miss_A_15_L2_blowfish  [0.0012, 0.0021, 0.0021, 0.0023, 0.0156]


A7_power_dijkstra = A7_proc_power + (1 + p_rw_dijkstra) * A7_L1_power + \
    (miss_A_7_IL1_dijkstra + p_rw_dijkstra * miss_A_7_DL1_dijkstra) * A7_L2_power 
A7_power_blowfish = A7_proc_power + (1 + p_rw_blowfish) * A7_L1_power + \
    (miss_A_7_IL1_blowfish + p_rw_blowfish * miss_A_7_DL1_blowfish) * A7_L2_power 
    
A15_power_dijkstra = A15_proc_power + (1 + p_rw_dijkstra) * A15_L1_power + \
    (miss_A_7_IL1_dijkstra + p_rw_dijkstra * miss_A_7_DL1_dijkstra) * A15_L2_power 
A15_power_blowfish = A15_proc_power + (1 + p_rw_blowfish) * A15_L1_power + \
    (miss_A_7_IL1_blowfish + p_rw_blowfish * miss_A_7_DL1_blowfish) * A15_L2_power 


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
ax.set_title("Energy Efficiency")

plt.show()





