from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#26A7FF"
    c1: str = "#7828FD"
    c2: str = "#FF5126"
    c3: str = "#FDF028"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    n: int = 12
    m: int = 12
    k: int = 0
    col: list[str] = [c1, c2, c3]
    t: np.ndarray = np.array([0])
    r: np.ndarray
    x: np.ndarray
    y: np.ndarray
    for i in range(n):
        for j in range(m):
            t = t[-1] + np.linspace(0, 2/m*np.pi, 600, endpoint=True)
            r = 0.5 * t + 0.125 * t * np.cos(6.0*t)
            x = r * np.sin(t)
            y = r * np.cos(t)
            ax.plot(x, y, linewidth=6, color=col[k%3])
            k += 1
    # arrange
    #ax.set_xlim(-1, 11)
    #ax.set_ylim(-2, 6)
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
