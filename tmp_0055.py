from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    c0: str = "#01B3ED"
    c1: str = "#B34E7E"
    c2: str = "#FFF8B8"
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 361, endpoint=True)
    r: float = 0.2
    x: np.ndarray = r * np.cos(t)
    y: np.ndarray = r * np.sin(t)

    h: float = 2.5
    th: np.ndarray
    c: np.ndarray
    s: np.ndarray

    th = np.linspace(-2*np.pi, 2*np.pi, 2001, endpoint=True)
    c = h * np.cos(th)
    s = h * np.sin(th)
    ax.plot(th, c, color=c2, linewidth=12)
    ax.plot(th, s, color=c2, linewidth=12)

    th = np.linspace(-2*np.pi, 2*np.pi, 101, endpoint=True)
    c = h*np.cos(th)
    s = h*np.sin(th)
    for a, cy, sy in zip(th, c, s):
        ax.plot(x+a, y+cy, color=c1, linewidth=6)
        ax.plot(x+a, y+sy, color=c1, linewidth=6)

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
