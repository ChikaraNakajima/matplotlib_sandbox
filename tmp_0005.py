from pathlib import Path

import numpy as np

from template_plt import plt


alpha: float = 0.0083
sigma: float = 0.1
mu: float = -0.38


def g1(x: np.ndarray) -> np.ndarray:
    return mu*x + 2.0*(1.0-mu)*x*x/(1.0+x*x)


def g2(x: np.ndarray) -> np.ndarray:
    return mu*x + (1.0-mu)*x*x*np.exp(0.25*(1.0-x*x))


def f2_g1(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    nx: np.ndarray = y + alpha*y*(1.0-sigma*y*y) + g1(x)
    ny: np.ndarray = -x + g1(nx)
    return nx, ny


def f2_g2(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    nx: np.ndarray = y + alpha*y*(1.0-sigma*y*y) + g2(x)
    ny: np.ndarray = -x + g2(nx)
    return nx, ny


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    x: np.ndarray
    y: np.ndarray
    rng: np.random.Generator = np.random.default_rng()
    x, y = rng.random((2, 100000))
    for i in range(200):
        x, y = f2_g2(x, y)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, linestyle="", marker=".", color=c1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(c0)
    fig.set_facecolor(c0)
    fig.tight_layout()
    fig.savefig(fp, facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
