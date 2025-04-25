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
    col: list[str] = [c1, c2]
    x: np.ndarray = np.array([1, 1, -1, -1, 1])
    y: np.ndarray = np.array([1, -1, -1, 1, 1])
    for i in range(2):
        for j in range(2):
            ci = 2*i-1
            cj = 2*j-1
            for k in range(11):
                c: float = 1.1 + 0.05*k
                r: float = 1 - 0.1*k
                ax.plot(r*x+c*ci, r*y+c*cj, color=col[(i+j+k)%2], linewidth=6)
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
