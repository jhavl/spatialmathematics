import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb
import numpy as np

pose_w = sm.SE2(0.0, 0.0, 0.0)
pose_a = sm.SE2(0.0, 0.0, -15 * np.pi / 180)
pose = sm.SE2(1.0, 2.0, 0.0)

plt.figure()

# ax = smb.trplot2(
#     pose_w.A,
#     frame="0",
#     color="#4287f5",
#     textcolor="#4287f5",
#     axissubscript=False,
#     length=0,
#     originsize=100,
# )

ax = smb.trplot2(
    pose_w.A,
    frame="0",
    dims=[-2, 3],
    color="#4287f5",
    textcolor="#4287f5",
    axissubscript=True,
    labels=("\hat{x}", "\hat{y}"),
)

smb.trplot2(
    pose_a.A,
    frame="a",
    dims=[-2, 3],
    color="#f58442",
    textcolor="#f58442",
    axissubscript=True,
    labels=("\hat{x}", "\hat{y}"),
)

circle = plt.Circle((1, 2), 0.1, color="#a6a6a6", fill=True)
ax.add_patch(circle)

ax.plot([0, 1], [0, 2], ":", color="#ababab")


ax.yaxis.label.set_color("#ababab")
ax.tick_params(axis="y", colors="#ababab")
ax.xaxis.label.set_color("#ababab")
ax.tick_params(axis="x", colors="#ababab")

ax.spines["right"].set_linewidth(0.0)
ax.spines["top"].set_linewidth(0.0)
ax.spines["bottom"].set_color("#ababab")
ax.spines["left"].set_color("#ababab")

ax.spines["bottom"].set_color("#525252")
ax.spines["left"].set_color("#525252")
ax.spines["bottom"].set_linewidth(0.5)
ax.spines["left"].set_linewidth(0.5)

ax.grid(color="#525252", linewidth=0.5)

plt.xlabel("$x_0$", fontsize=14)
plt.ylabel("$y_0$", fontsize=14)


plt.savefig("Module 1/Tutorial/Figures/fig2-2a.png", transparent=True)
