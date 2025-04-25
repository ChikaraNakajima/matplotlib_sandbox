from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def parabola(x: float|np.ndarray, p: float) -> float|np.ndarray:
    return x*x/(4*p)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#5B7A97"
    c1: str = "#B7EB21"
    c2: str = "#60B683"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    p: float = 0.5
    l: float = 1.0
    for i in np.linspace(-0.9*l, 0.9*l, 12, endpoint=True):
        px: list[float] = [-3, -parabola(i, p), -p]
        py: list[float] = [i, i, 0]
        ax.plot(px, py, linewidth=6, color=c2)
    y: np.ndarray[np.float64] = np.linspace(-l, l, 10001, endpoint=True)
    x: np.ndarray = -parabola(y, p)
    ax.plot(x, y, linewidth=6, color=c1)
    ax.plot([-p], [0], linestyle="", marker="o",color=c2, markersize=6)
    # arrange
    #ax.set_xlim(-1.1*p, 1.1*p)
    ax.set_ylim(-1.1*l, 1.1*l)
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
