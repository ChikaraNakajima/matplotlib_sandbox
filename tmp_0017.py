import math
import random
from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    x: list[float] = [0]
    y: list[float] = [1]
    n: int = 6
    r: float = 2/n
    lx: list[float] = [math.sin(2.0*math.pi*i/n) for i in range(n)]
    ly: list[float] = [math.cos(2.0*math.pi*i/n) for i in range(n)]
    for i in range(100000):
        index: int = random.randint(0, n-1)
        x.append(r*x[-1]+(1-r)*lx[index])
        y.append(r*y[-1]+(1-r)*ly[index])
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
