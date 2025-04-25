from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#FFE4A8"
    c1: str = "#008B52"
    c2: str = "#412554"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 2001, endpoint=True)
    n: int = 24
    col: list[str] = [c1, c2]
    r: np.ndarray
    x: np.ndarray
    y: np.ndarray
    for i in range(n):
        r = 1 + (1+i)/n * np.cos(6*t + (1+i)/n*np.pi)
        x = r * np.cos(t)
        y = r * np.sin(t)
        ax.plot(x, y, linewidth=6, color=col[i%2])
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
