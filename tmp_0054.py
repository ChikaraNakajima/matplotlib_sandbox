from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#E66C4F"
    c1: str = "#64DB8F"
    c2: str = "#55A5FF"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray
    xp: np.ndarray
    xm: np.ndarray
    y: np.ndarray
    s: float = 2
    a: float = 1
    b: float = 1
    f: float = np.sqrt(a*a+b*b)

    t = np.linspace(-0.9*s, 0.9*s, 12, endpoint=True)
    xp = a*np.cosh(t)
    xm = -xp
    y = b*np.sinh(t)
    for i, j, k in zip(xp, xm, y):
        ax.plot([-f, i, f], [0, k, 0], color=c1, linewidth=6)
        ax.plot([-f, j, f], [0, k, 0], color=c1, linewidth=6)

    t = np.linspace(-s, s, 2001, endpoint=True)
    xp = a*np.cosh(t)
    xm = -xp
    y = b*np.sinh(t)
    ax.plot(xp, y, color=c2, linewidth=12)
    ax.plot(xm, y, color=c2, linewidth=12)
    ax.plot([f, -f], [0, 0], color=c2, linestyle="", marker="o", markersize=12)
    # arrange
    #ax.set_xlim(-1.1, 1.1)
    #ax.set_ylim(-1.1, 1.1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(c0)
    fig.set_facecolor(c0)
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
