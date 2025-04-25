import typing
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


alpha: float = 0.009
sigma: float = 0.05
mu: float = -0.801


def gm_g1(x: np.ndarray) -> np.ndarray:
    return mu*x + 2*(1-mu)*x*x/(1+x*x)


def gm_g2(x: np.ndarray) -> np.ndarray:
    return mu*x + (1-mu)*x*x*np.exp(0.25*(1-x*x))


def gm_f1(x: np.ndarray, y: np.ndarray, g: typing.Callable=gm_g1) -> tuple[np.ndarray, np.ndarray]:
    xn: np.ndarray = y + g(x)
    yn: np.ndarray = -x + g(xn)
    return xn, yn


def gm_f2(x: np.ndarray, y: np.ndarray, g: typing.Callable=gm_g1) -> tuple[np.ndarray, np.ndarray]:
    xn: np.ndarray = y + alpha*y*(1-sigma*y*y) + g(x)
    yn: np.ndarray = -x + g(xn)
    return xn, yn


def hsv2rgb(h: float, s: float, v: float) -> str:
    rgb: np.ndarray = np.round(255 * ((np.clip(np.abs(np.modf(h + np.array([0, 2, 1]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    bgc: str = hsv2rgb(0.875, 0.5, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    x: np.ndarray
    y: np.ndarray
    rng: np.random.Generator = np.random.default_rng()
    x, y = rng.random((2, 1000000))
    for _ in range(100):
        x, y = gm_f2(x, y)
    ax.plot(x, y, linestyle="", marker=".", color=hsv2rgb(0.375, 0.5, 1.0))
    # arrange
    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(bgc)
    fig.set_facecolor(bgc)
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
