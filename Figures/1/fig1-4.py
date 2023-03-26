import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose_w = sm.SE2(0.0, 0.0, 0.0)
pose2 = sm.SE2(3.0, 1.0, 0.0)

plt.figure()


ax = smb.trplot2(
    pose_w.A,
    dims=[-1.0, 4.0],
    frame="0",
    color="#4287f5",
    textcolor="#4287f5",
    originsize=0,
    origincolor="#4287f5",
    axissubscript=True,
    labels=("\hat{x}", "\hat{y}"),
    rviz=False,
)

smb.trplot2(
    pose2.A,
    dims=[-1.0, 4.0],
    frame="a",
    color="#f58442",
    textcolor="#f58442",
    originsize=0,
    origincolor="#f58442",
    axissubscript=True,
    labels=("\hat{x}", "\hat{y}"),
    rviz=False,
)

# ax.plot([0, 3], [0, 1], ":", color="#ababab")

ax.quiver(
    0,
    0,
    3,
    1,
    angles="xy",
    scale_units="xy",
    scale=1,
    linewidth=0.2,
    facecolor="#ababab",
    edgecolor="#ababab",
)


ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")

ax.spines["right"].set_linewidth(0.0)
ax.spines["top"].set_linewidth(0.0)
ax.spines["bottom"].set_color("#ababab")
ax.spines["left"].set_color("#ababab")

ax.grid(color="#525252", linewidth=0.5)

plt.xlabel("$x$", fontsize=14)
plt.ylabel("$y$", fontsize=14)


ax.spines["bottom"].set_color("#525252")
ax.spines["left"].set_color("#525252")
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["left"].set_linewidth(0.5)

ax.text(
    1.6,
    0.9,
    r"${^0\mathbf{t}_a}$",
    color="#ababab",
    verticalalignment="top",
    horizontalalignment="left",
)

plt.savefig("Module 1/Tutorial/Figures/fig1-4.png", transparent=True)
