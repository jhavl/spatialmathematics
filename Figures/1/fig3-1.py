import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose = sm.SE2(1.0, 2.0, 0.0)
pose2 = sm.SE2(3.0, 5.0, 0.0)

plt.figure()

ax = smb.trplot2(
    pose.A,
    dims=[0, 5.4],
    color="#4287f5",
    textcolor="#4287f5",
    block=False,
    rviz=False,
    originsize=200,
    axislabel=False,
    length=0,
)

smb.trplot2(
    pose2.A,
    dims=[0, 5.4],
    color="#4287f5",
    textcolor="#4287f5",
    block=False,
    rviz=False,
    originsize=200,
    axislabel=False,
    length=0,
)

# ax.plot([0, 1], [2, 2], ":", color="#ababab")
# ax.plot([1, 1], [0, 2], ":", color="#ababab")

ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")

ax.spines["right"].set_linewidth(0.0)
ax.spines["top"].set_linewidth(0.0)
ax.spines["bottom"].set_color("#ababab")
ax.spines["left"].set_color("#ababab")

ax.grid(color="#525252", linewidth=0.5)

plt.savefig("Module 1/Tutorial/Figures/fig3-1.png", transparent=True)
