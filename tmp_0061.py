from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色アイディア手帖 90
    colors: list[str] = [
        "#f5e49e",
        "#ca9170",
        "#dec39c",
        "#d3d1bd",
        "#d56950",
        "#4b4846",
        "#89a3d3",
        "#e0e565",
        "#d82630",
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    n: int = 13
    for i in range(1+n//2, 0, -1):
        t: np.ndarray = np.linspace(0, 2*np.pi*i, n+1, endpoint=True)
        c: np.ndarray = np.cos(t)
        s: np.ndarray = np.sin(t)
        ax.plot(s, -c, linewidth=12, color=colors[i])
    # arrange
    #ax.set_xlim(-1, 11)
    #ax.set_ylim(-2, 6)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(colors[0])
    fig.set_facecolor(colors[0])
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
