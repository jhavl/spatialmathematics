import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose_w = sm.SE2(0.0, 0.0, 0.0)
pose = sm.SE2(1.0, 2.0, 0.0)
pose2 = sm.SE2(3.0, 1.0, 0.0)

plt.figure()

ax = smb.trplot2(
    pose_w.A,
    frame="0",
    color="#4287f5",
    textcolor="#4287f5",
    axissubscript=True,
    labels=("\hat{x}", "\hat{y}"),
)

# ax = smb.trplot2(
#     pose.A,
#     dims=[-1.0, 4.0],
#     color="#4287f5",
#     textcolor="#4287f5",
#     block=False,
#     rviz=False,
#     originsize=200,
#     axislabel=False,
#     length=0,
# )

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

circle = plt.Circle((1, 2), 0.1, color="#a6a6a6", fill=True)
ax.add_patch(circle)


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

ax.quiver(
    0.1,
    0.1,
    0.8,
    1.8,
    angles="xy",
    scale_units="xy",
    scale=1,
    linewidth=0.2,
    facecolor="#4287f5",
    edgecolor="#4287f5",
)

ax.quiver(
    2.9,
    1.1,
    -1.75,
    0.83,
    angles="xy",
    scale_units="xy",
    scale=1,
    linewidth=0.2,
    facecolor="#f58442",
    edgecolor="#f58442",
)

ax.text(
    2,
    1.8,
    r"${^a\mathbf{p}}$",
    color="#f58442",
    verticalalignment="top",
    horizontalalignment="left",
)

ax.text(
    0.35,
    1.5,
    r"${^0\mathbf{p}}$",
    color="#4287f5",
    verticalalignment="top",
    horizontalalignment="left",
)

plt.savefig("Module 1/Tutorial/Figures/fig1-3.png", transparent=True)
