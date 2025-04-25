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
    col: list[str] = [c1, c2]
    rng: np.random.Generator = np.random.default_rng()
    data: list[list[float]] = [
        [2*(2*rng.random()-1), 2*(2*rng.random()-1), 0.1*rng.random()]
        for i in range(640)
    ]
    t: np.ndarray = np.linspace(0, 2*np.pi, 361, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for i, (x, y, r) in enumerate(data):
        ax.plot(r*c+x, r*s+y, linewidth=6, color=col[i%2])
    # arrange
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-0.9, 0.9)
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
