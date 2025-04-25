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
    t: np.ndarray = np.linspace(0, 2*np.pi, 361, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for i in range(16):
        for j in range(9):
            lc: str = col[(i+j)%2]
            for k in range(4):
                r: float = 0.25 * (k+1)/4
                ax.plot(r*c+i, r*s+j, linewidth=2, color=lc)
    t: np.ndarray = np.linspace(0, 2*np.pi, 5, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for i in range(15):
        for j in range(8):
            lc: str = col[(i+j)%2]
            for k in range(3):
                r: float = 0.25 * np.sqrt(2) * (k+1)/3
                ax.plot(r*c+i+0.5, r*s+j+0.5, linewidth=2, color=lc)
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
