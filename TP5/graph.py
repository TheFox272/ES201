import matplotlib.pyplot as plt
import numpy as np
import re


# def parse_file(file_path, one_cpu):
#     with open(file_path, 'r') as file:
#         data = file.read()

#     if not one_cpu:
#         numCycle = re.findall(r'system\.cpu0\.numCycles\s*(\d+)', data)
#     else:
#         numCycle = re.findall(r'system\.cpu\.numCycles\s*(\d+)', data)

#     numInstr = re.findall(r'sim_insts\s*(\d+)', data)

#     return numCycle, numInstr

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Provided data
n_threads = [1, 2, 4, 8, 16]
n_voies = [2, 4, 8]
n_cycles = np.array([[111977, 97855, 89573, 88817, 95709],
            [92759, 86637, 83467, 84207, 89939],
            [91408, 85464, 82546, None, 89899]]).T
n_instructions = np.array([[86730, 101143, 123744, 179214, 378453],
                  [92172, 108485, 149794, 235986, 495586],
                  [86730, 116470, 174986, None, 677009]]).T

speedup = np.array([[n_cycles[0][0] / n_cycles[i][j] if n_cycles[i][j] is not None else None for j in range(len(n_voies))] for i in range(len(n_threads))])
ipc = np.array([[n_instructions[i][j] / n_cycles[i][j] if n_cycles[i][j] is not None else None for j in range(len(n_voies))] for i in range(len(n_threads))])

# Create meshgrid for 3D plotting
n_voies, n_threads = np.meshgrid(n_voies, n_threads)

# Plotting n_cycles with exchanged x and y axes
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(n_threads, n_voies, n_cycles, cmap='viridis')
ax1.set_ylabel('n_voies')
ax1.set_xlabel('n_threads')
ax1.set_zlabel('n_cycles')
ax1.set_title('3D Plot for n_cycles')
ax1.set_facecolor('lightgrey')
ax1.grid(True)
ax1.view_init(30, -10)
cbar1 = fig1.colorbar(ax1.plot_surface(n_threads, n_voies, n_cycles, cmap='viridis'), ax=ax1, pad=0.1)
cbar1.set_label('n_cycles')

# Plotting speedup with exchanged x and y axes
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(n_threads, n_voies, speedup, cmap='viridis')
ax2.set_ylabel('n_voies')
ax2.set_xlabel('n_threads')
ax2.set_zlabel('speedup')
ax2.set_title('3D Plot for speedup')
ax2.set_facecolor('lightgrey')
ax2.grid(True)
ax2.view_init(30, -100)
cbar2 = fig2.colorbar(ax2.plot_surface(n_threads, n_voies, speedup, cmap='viridis'), ax=ax2, pad=0.1)
cbar2.set_label('Speedup')

# Plotting ipc with exchanged x and y axes
fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot_surface(n_threads, n_voies, ipc, cmap='viridis')
ax3.set_ylabel('n_voies')
ax3.set_xlabel('n_threads')
ax3.set_zlabel('ipc')
ax3.set_title('3D Plot for IPC')
ax3.set_facecolor('lightgrey')
ax3.grid(True)
ax3.view_init(30, -60)
cbar3 = fig3.colorbar(ax3.plot_surface(n_threads, n_voies, ipc, cmap='viridis'), ax=ax3, pad=0.1)
cbar3.set_label('IPC')

# Adjust subplot spacing
plt.subplots_adjust(wspace=0.4)

# Save the figures
fig1.savefig('n_cycles_plot.png')
fig2.savefig('speedup_plot.png')
fig3.savefig('ipc_plot.png')

# Show the plots
plt.show()
