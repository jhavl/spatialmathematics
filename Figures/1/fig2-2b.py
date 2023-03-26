import spatialmath as sm
import matplotlib.pyplot as plt
import spatialmath.base as smb

pose_w = sm.SE2(-10.0, 0.0, 0.0)
pose = sm.SE2(1.0, 2.0, 0.0)

plt.figure()

ax = smb.trplot2(
    pose_w.A,
    color="#4287f5",
    textcolor="#4287f5",
    axissubscript=False,
    axislabel=False,
    length=0,
    originsize=0,
    dims=[-2.0, 3.0],
    labels=["", ""],
)

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

plt.xlabel("$x_a$", fontsize=14)
plt.ylabel("$y_a$", fontsize=14)

plt.savefig("Module 1/Tutorial/Figures/fig2-2b.png", transparent=True)
