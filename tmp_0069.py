from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色バリエーション BOOK 3
    colors: list[str] = [
        f"#{r:02x}{g:02x}{b:02x}"
        for r, g, b in [
            (65, 127, 100),
            (213, 221, 94),
        ]
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    rng: np.random.Generator = np.random.default_rng()
    points: list[np.ndarray] = [2*rng.random(2)-1 for i in range(10000)]
    mapping: list[list[np.ndarray]] = [
        [np.array([[0, 0], [0, 0.16]]), np.array([0, 0])],
        [np.array([[0.85, 0.04], [-0.04, 0.85]]), np.array([0, 1.6])],
        [np.array([[0.20, -0.26], [0.23, 0.22]]), np.array([0, 1.6])],
        [np.array([[-0.15, 0.28], [0.26, 0.24]]), np.array([0, 0.44])],
    ]
    mpindex: list[int] = [0, 1, 2, 3]
    probability: list[float] = [0.01, 0.85, 0.07, 0.07]
    for i in range(1000):
        for j, p in enumerate(points):
            m: np.ndarray
            v: np.ndarray
            index: int = rng.choice(mpindex, 1, p=probability)[0]
            m, v = mapping[index]
            points[j] = m @ p + v
    x: np.ndarray
    y: np.ndarray
    x, y = np.array(points).T
    ax.plot(x, y, linestyle="", marker="o", color=colors[0])
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
