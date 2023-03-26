import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose_w = sm.SE2(0.0, 0.0, 0.0)
pose = sm.SE2(1.0, 2.0, 0.0)
pose2 = sm.SE2(3.0, 1.0, 0.0)

plt.figure()

ax = smb.trplot2(
    pose_w.A,
    dims=[-1.0, 4.0],
    color="#4287f5",
    textcolor="#4287f5",
    axissubscript=False,
    length=0,
    axislabel=False,
    originsize=0
    # labels=("\hat{x}", "\hat{y}"),
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

plt.xlabel("", fontsize=14)
plt.ylabel("", fontsize=14)

ax.spines["bottom"].set_color("#525252")
ax.spines["left"].set_color("#525252")
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["left"].set_linewidth(0.5)

ax.quiver(
    0.0,
    0.0,
    0.866,
    0.5,
    angles="xy",
    scale_units="xy",
    scale=1,
    linewidth=0.2,
    facecolor="#4287f5",
    edgecolor="#4287f5",
)

ax.quiver(
    0.0,
    0.0,
    -0.5,
    0.866,
    angles="xy",
    scale_units="xy",
    scale=1,
    linewidth=0.2,
    facecolor="#4287f5",
    edgecolor="#4287f5",
)

ax.text(
    0.6,
    0.25,
    r"$\hat{x}$",
    color="#4287f5",
    verticalalignment="top",
    horizontalalignment="left",
)

ax.text(
    -0.45,
    0.4,
    r"$\hat{y}$",
    color="#4287f5",
    verticalalignment="top",
    horizontalalignment="left",
)

plt.savefig("Module 2/Tutorial/Figures/fig1-3.png", transparent=True)
