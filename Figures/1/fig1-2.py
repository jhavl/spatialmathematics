import roboticstoolbox as rtb
from swift import Swift
import spatialgeometry as sg
import spatialmath as sm
import matplotlib.pyplot as plt
import matplotlib as mpl
import spatialmath.base as smb


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


pose = sm.SE3(3.0, 2.0, 4.0)
plt.figure()
ax = smb.trplot(
    pose.A,
    dims=[0, 5.5],
    color="#4287f5",
    textcolor="#4287f5",
    block=False,
    rviz=False,
    originsize=200,
    width=1.5,
    length=0,
)

ax.plot([3, 3], [2, 2], [0, 4], ":", color="#ababab", linewidth=1.0)
ax.plot([0, 3], [2, 2], [4, 4], ":", color="#ababab", linewidth=1.0)
ax.plot([3, 3], [2, 5.4], [4, 4], ":", color="#ababab", linewidth=1.0)

ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")
ax.zaxis.label.set_color("#ababab")
ax.tick_params(axis="z", colors="#ababab")

ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False


plt.xlabel("$x$", fontsize=10)
plt.ylabel("$y$", fontsize=10)
ax.set_zlabel("$z$", fontsize=10)

ax.xaxis.get_ticklines()[3].set_color("#4287f5")
ax.xaxis.get_ticklabels()[3].set_color("#4287f5")

ax.yaxis.get_ticklines()[2].set_color("#4287f5")
ax.yaxis.get_ticklabels()[2].set_color("#4287f5")

ax.zaxis.get_ticklines()[4].set_color("#4287f5")
ax.zaxis.get_ticklabels()[4].set_color("#4287f5")

plt.savefig("Module 1/Tutorial/Figures/fig1-2.png", transparent=True)
