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
    n: int = 7
    t: np.ndarray = np.linspace(0, n*2*np.pi, n*3600+1, endpoint=True)
    for i in range(1, 1+n//2):
        rm: float = i/n
        y: np.ndarray = (1-rm)*np.cos(t) + rm*np.cos((1/rm-1)*t)
        x: np.ndarray = (1-rm)*np.sin(t) - rm*np.sin((1/rm-1)*t)
        ax.plot(x, -y, color=c1, linewidth=6)
    ax.plot(np.cos(t), np.sin(t), color=c2, linewidth=12)
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
