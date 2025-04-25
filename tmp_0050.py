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
    t: np.ndarray = np.linspace(-4*np.pi, 4*np.pi, 2001, endpoint=True)
    c: np.ndarray
    s: np.ndarray
    th: np.ndarray
    n: int = 13
    for i in range(n):
        th = (0.5+0.5*i/n)*t
        c = 6*np.cos(th)
        s = 6*np.sin(th)
        ax.plot(t, c, linewidth=6, color=c1)
        ax.plot(t, s, linewidth=6, color=c2)
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
