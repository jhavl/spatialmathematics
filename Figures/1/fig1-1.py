import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose = sm.SE2(1.0, 2.0, 0.0)
plt.figure()


ax = smb.trplot2(
    pose.A,
    dims=[-1, 4],
    color="#4287f5",
    textcolor="#4287f5",
    block=False,
    rviz=False,
    originsize=0,
    axislabel=False,
    length=0,
)

circle = plt.Circle((1, 2), 0.1, color="#4287f5", fill=True)

ax.add_patch(circle)

ax.plot([0, 1], [2, 2], ":", color="#ababab")
ax.plot([1, 1], [0, 2], ":", color="#ababab")

ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")

ax.spines["right"].set_linewidth(0.0)
ax.spines["top"].set_linewidth(0.0)

ax.spines["bottom"].set_color("#525252")
ax.spines["left"].set_color("#525252")
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["left"].set_linewidth(0.5)

ax.grid(color="#525252", linewidth=0.5)

gridx = ax.get_xgridlines()
gridy = ax.get_ygridlines()
gridx[1].set_linewidth(1.0)
gridy[1].set_linewidth(1.0)
gridx[1].set_color("#ababab")
gridy[1].set_color("#ababab")

plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)

ax.xaxis.get_ticklines()[2].set_color("#4287f5")
ax.xaxis.get_ticklabels()[2].set_color("#4287f5")

ax.yaxis.get_ticklines()[3].set_color("#4287f5")
ax.yaxis.get_ticklabels()[3].set_color("#4287f5")

plt.savefig("Module 1/Tutorial/Figures/fig1-1.png", transparent=True)
