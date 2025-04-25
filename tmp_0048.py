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
    for i in range(16):
        for j in range(9):
            o: int = (i+j)%2
            for k in range(8):
                r: float = 0.8*0.0625*(k+1)
                ax.plot(r*x+i, r*y+j, color=col[(k+o)%2], linewidth=2)
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
