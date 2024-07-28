import math
import random
from pathlib import Path

import numpy as np

from template_plt import plt


sigma: float = 10.0
rho: float = 28.0
beta: float = 8.0 / 3.0
dt: float = 1.0e-4


def lorenz(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    dx: np.ndarray = sigma*(y-x)
    dy: np.ndarray = x*(rho-z)-y
    dz: np.ndarray = x*y-beta*z
    dx *= dt
    dy *= dt
    dz *= dt
    x += dx
    y += dy
    z += dz
    return x, y, z


def main() -> None:
    home: Path = Path(__file__).resolve().parent
    fstem = Path(__file__).resolve().stem
    c0: str = "#29292E"
    c1: str = "#E06B22"
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    rng: np.random.Generator = np.random.default_rng()
    x, y, z = rng.random((3, 10000))
    for i in range(1000000):
        x, y, z = lorenz(x, y, z)
        print(i)
    xyz: dict[str, np.ndarray] = {"x": x, "y": y, "z": z}
    names: list[str] = ["xy", "yz", "zx"]
    for name in names:
        fig: plt.Figure
        ax: plt.Axes
        fig, ax = plt.subplots()
        ax.plot(xyz[name[0]], xyz[name[1]], linestyle="", marker=".", color=c1)
        ax.axis("off")
        ax.set_aspect("equal")
        ax.set_facecolor(c0)
        fig.set_facecolor(c0)
        fig.tight_layout()
        fig.savefig(home.joinpath(fstem+"_"+name+".png"), facecolor=fig.get_facecolor())
        plt.cla()
        plt.clf()
        plt.close(fig)
    return None


if __name__ == "__main__":
    main()
