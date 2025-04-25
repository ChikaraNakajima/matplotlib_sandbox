from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色バリエーション BOOK 2
    colors: list[str] = [
        "#DB7307",
        "#F9F790",
        "#64DB8F",
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 2001, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for i in range(16):
        for j in range(9):
            for k in range(2):
                th: float = np.pi * 0.125 * (i-j) + np.pi * 0.25 * k
                cos: float = np.cos(th)
                sin: float = np.sin(th)
                m: np.ndarray = np.array([[cos, -sin], [sin, cos]])
                r: float = 0.4
                x: np.ndarray = r * c
                y: np.ndarray = 0.5 * r * s
                x, y = m @ np.array([x, y])
                ax.plot(x+i, y+j, color=colors[(i+j+k)%2], linewidth=6)
            ax.plot([i], [j], color=colors[(i+j)%2], linestyle="", marker="o")
    # arrange
    #ax.set_xlim(-np.pi, np.pi)
    #ax.set_ylim(-1, 1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(colors[-1])
    fig.set_facecolor(colors[-1])
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
