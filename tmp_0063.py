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
        f"#{r:02x}{g:02x}{b:02x}"
        for r, g, b in [
            (200, 219, 128),
            (216, 184, 214),
            (83, 179, 129),
            (147, 195, 233),
            (158, 162, 78),
            (253, 251, 213),
            (165, 189, 226),
            (198, 230, 229),
            (59, 163, 203),
            (98, 190, 192),
        ]
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 361, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    rng: np.random.Generator = np.random.default_rng()
    for i in range(9):
        color: str = colors[i]
        for j in range(24):
            r: float = rng.random() * 1e-1
            x: float = rng.random()
            y: float = rng.random()
            x = 2*x-1
            y = 2*y-1
            ax.plot(r*c+x, r*s+y, color=color, linewidth=6)
    # arrange
    ax.set_xlim(-0.95, 0.95)
    ax.set_ylim(-0.95*9/16, 0.95*9/16)
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
