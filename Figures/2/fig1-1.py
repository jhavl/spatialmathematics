import roboticstoolbox as rtb
import spatialgeometry as sg
import spatialmath as sm
import matplotlib.pyplot as plt
import matplotlib as mpl
import spatialmath.base as smb
import numpy as np


mpl.rcParams["axes.linewidth"] = -1
mpl.rcParams["xtick.color"] = "#ababab"
mpl.rcParams["ytick.color"] = "#ababab"
# mpl.rcParams["xtick.major.size"] = 0
# mpl.rcParams["ytick.major.size"] = 0
mpl.rcParams["xtick.major.width"] = 0
mpl.rcParams["ytick.major.width"] = 0
# mpl.rcParams["xtick.minor.size"] = 0
# mpl.rcParams["ytick.minor.size"] = 0
mpl.rcParams["grid.linewidth"] = 0.3

# Turn off spines
mpl.rcParams["axes.autolimit_mode"] = "round_numbers"
mpl.rcParams["axes.xmargin"] = 1.0
# mpl.rcParams["axes.spines.bottom"] = False
# mpl.rcParams["axes.spines.left"] = False

ax = plt.figure().add_subplot(projection="3d")

# Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1
coefs = (1, 1, 1)

# Radii corresponding to the coefficients:
rx, ry, rz = 1 / np.sqrt(coefs)

# Set of all spherical angles:
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

# Plot:
ax.plot_surface(x, y, z, rstride=1, cstride=1, color="#4287f5")

# Adjustment of the axes, so that they all have the same span:
max_radius = max(rx, ry, rz)
for axis in "xyz":
    getattr(ax, "set_{}lim".format(axis))((-max_radius, max_radius))

ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")
ax.zaxis.label.set_color("#ababab")
ax.tick_params(axis="z", colors="#ababab")

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# ax.grid(False)

plt.savefig("Module 2/Tutorial/Figures/fig1-1.png", transparent=True)
