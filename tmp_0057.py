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
    t: np.ndarray = np.linspace(-2*np.pi, 2*np.pi, 2001, endpoint=True)
    c: np.ndarray
    s: np.ndarray
    th: np.ndarray
    n: int = 32
    w: float = 2
    for i in range(n):
        th = t*((1+i)/n)
        c = w*np.cos(th)
        s = w*np.sin(th)
        ax.plot(t, c, color=c1, linewidth=6)
        ax.plot(t, s, color=c2, linewidth=6)
    # arrange
    #ax.set_xlim(-1.6, 1.6)
    #ax.set_ylim(-0.9, 0.9)
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
