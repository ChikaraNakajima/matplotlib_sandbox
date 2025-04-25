from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色バリエーション BOOK 23
    colors: list[str] = [
        f"#{r:02x}{g:02x}{b:02x}"
        for r, g, b in [
            [119, 150, 73],

            [133, 142, 197],
            [0, 37, 73],
            [188, 191, 219],
            [92, 131, 176],
            [115, 187, 198],

            [12, 68, 150],
            [50, 84, 164],
            [206, 217, 207],
            [126, 103, 55],
            [153, 162, 86],

            [211, 191, 165],
            [245, 229, 169],
            [179, 185, 99],
            [67, 141, 199],
            [0, 79, 153],

            [58, 123, 120],
            [151, 142, 112],
            [171, 144, 34],
            [214, 223, 228],
            [80, 89, 41],

            [129, 69, 40],
            [134, 179, 224],
            [77, 108, 64],
            [85, 46, 39]
        ]
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 3601, endpoint=True)
    for i, c in enumerate(colors[:-1]):
        r: np.ndarray = 1 + (1+i)/24 * np.cos(t*6+2*np.pi*i/24)
        x: np.ndarray = r * np.sin(t)
        y: np.ndarray = r * np.cos(t)
        for j in range(3):
            for k in range(2):
                ax.plot(0.2*x+j, 0.2*y+k, color=c, linewidth=6)
    # arrange
    #ax.set_xlim(-np.pi, np.pi)
    #ax.set_ylim(-np.pi*9/8, np.pi*9/8)
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
