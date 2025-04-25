from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色バリエーション BOOK 24
    colors: list[str] = [
        f"#{r:02x}{g:02x}{b:02x}"
        for r, g, b in [
            (120, 147, 81),
            (161, 184, 174),
            (219, 112, 25),
            (182, 131, 79),
            (147, 33, 45),
        ]
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(-2*np.pi, 2*np.pi, 2001, endpoint=True)
    ax.plot([-2*np.pi, 2*np.pi], [0, 0], color=colors[0], linewidth=6)
    ax.plot([0, 0], [-np.pi*9/8, np.pi*9/8], color=colors[0], linewidth=6)
    ax.plot(t, np.cosh(t), color=colors[1], linewidth=6)
    ax.plot(t, np.sinh(t), color=colors[2], linewidth=6)
    ax.plot(t, np.tanh(t), color=colors[3], linewidth=6)
    # arrange
    #ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-np.pi*9/8, np.pi*9/8)
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
