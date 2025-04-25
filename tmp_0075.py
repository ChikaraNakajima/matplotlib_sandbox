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
    w: float = 18
    a: float = 0.5
    t: np.ndarray = np.linspace(-2*np.pi, 2*np.pi, 3601, endpoint=True)
    y = 4 * np.cos(a*t)
    ax.plot(t, y, linewidth=6, color=colors[1])
    ax.plot(t, -y, linewidth=6, color=colors[3])
    y: np.ndarray = np.cos((w-a)*t) + np.cos((w+a)*t)
    y *= 2
    ax.plot(t, y, linewidth=6, color=colors[0])
    # arrange
    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
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
