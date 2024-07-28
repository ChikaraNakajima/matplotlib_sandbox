import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(x: np.ndarray, y: np.ndarray) -> None:
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, linestyle="", marker=".", color="#E06B22")
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor("#29292E")
    fig.set_facecolor("#29292E")
    fig.tight_layout()
    fig.savefig(Path(__file__).resolve().with_suffix(".png"), facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


alpha: float = 0.009
sigma: float = 0.05
mu: float = -0.801


def g1(x: np.ndarray) -> np.ndarray:
    return mu*x + 2.0*(1.0-mu)*x*x/(1.0+x*x)


def f2_g1(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    nx: np.ndarray = y + alpha*y*(1.0-sigma*y*y) + g1(x)
    ny: np.ndarray = -x + g1(nx)
    return nx, ny


def main() -> None:
    x: np.ndarray
    y: np.ndarray
    rng: np.random.Generator = np.random.default_rng()
    x, y = rng.random((2, 1000000))
    for i in range(100):
        x, y = f2_g1(x, y)
    make_graph(x, y)
    return None


if __name__ == "__main__":
    main()
