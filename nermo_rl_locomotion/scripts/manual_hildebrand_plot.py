import numpy as np
import seaborn
import matplotlib.pyplot as plt

# Activate seaborn
seaborn.set()

fig, ax = plt.subplots()

# Data for the stance phases (time in msec) depicted in the diagram of Hruska et al. 1979 - Format for each phase: (t_begin, t_end)
foot_stance_phases = {
    "lh": [(0,143), (500, 643), (1000,1143), (1500,1643)],
    "lf": [(357,500), (857,1000), (1357,1500), (1857,2000)],
    "rf": [(357,500), (857,1000), (1357,1500), (1857,2000)],
    "rh": [(0,143), (500, 643), (1000,1143), (1500,1643)]
}
# Convert phases to format (t_begin, duration) required for matplotlib's `broken_barh` 
for foot, stance_phases in foot_stance_phases.items():
    foot_stance_phases[foot] = [(phase[0], phase[1] - phase[0]) for phase in foot_stance_phases[foot]]

# Scale phase times to seconds
time_scaling_factor = 1/1000
for foot, stance_phases in foot_stance_phases.items():
    foot_stance_phases[foot] = [(phase[0] * time_scaling_factor, phase[1] * time_scaling_factor) for phase in foot_stance_phases[foot]]


hildebrand_foot_order=["rh", "rf", "lf", "lh"]
t_start = 0
t_end = 2
time_unit = "sec"

for i, foot in enumerate(hildebrand_foot_order):
    ax.broken_barh(list(foot_stance_phases[foot]), ((i * 5) + 4, 2), facecolors='tab:blue')

ax.set_ylim(1, 24)
ax.set_xlim(t_start, t_end)
ax.set_xlabel(f"Time [{time_unit}]")
ax.set_yticks([5, 10, 15, 20])
ax.set_yticklabels([label.upper() for label in hildebrand_foot_order])
ax.grid(True)


plt.tight_layout()
plt.show()
