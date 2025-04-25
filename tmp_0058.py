from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#E76F53"
    c1: str = "#F1B9BA"
    c2: str = "#5C3B95"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(-2*np.pi, 2*np.pi, 2001, endpoint=True)
    th: np.ndarray = np.linspace(-2*np.pi, 2*np.pi, 2001, endpoint=True)
    w: float = 1
    h: float = w + 0.1
    c: np.ndarray
    s: np.ndarray
    for i in range(6):
        c = w*np.cos(th)
        s = w*np.sin(th)
        ax.plot(t, c+h, color=c1, linewidth=6)
        ax.plot(t, s-h, color=c2, linewidth=6)
        th *= 2
        w *= 0.5
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
