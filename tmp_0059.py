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
    col: list[str] = [c1, c2]
    prime_number: list[int] = [3, 5, 7, 11, 13, 17]#, 19, 23, 29]
    t: np.ndarray
    c: np.ndarray
    s: np.ndarray
    w: float = 0.45
    for i, p in enumerate(prime_number):
        for j in range(p//2+1):
            t = np.linspace(0, j*2*np.pi, 1+p, endpoint=True)
            c = w*np.cos(t)
            s = w*np.sin(t)
            ax.plot(s+j, -c+i, color=col[(i+j)%2], linewidth=6)
            ax.plot(s+10-j, c+4-i, color=col[(i+j)%2], linewidth=6)
    p: np.ndarray = np.array([1, -1])
    d: np.ndarray = p - np.array([9, 5])
    pm: np.ndarray = p - 2*d
    pp: np.ndarray = p + 2*d
    ax.plot([pm[0], pp[0]], [pm[1], pp[1]], color=c3, linewidth=12)
    # arrange
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 6)
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
