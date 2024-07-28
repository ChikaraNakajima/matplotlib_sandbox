import math
import random
from pathlib import Path

from template_plt import plt


d = 10000.0
d = -1.0/d


def levy_dust(x: float, y: float) -> tuple[float, float]:
    r: float = math.pow(1.0-random.random(), d)
    u: float = random.random() * 2.0 * math.pi
    x = x + r * math.cos(u)
    y = y + r * math.sin(u)
    return x, y


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    x: list[float] = [0]
    y: list[float] = [0]
    for i in range(100000):
        tx, ty = levy_dust(x[-1], y[-1])
        x.append(tx)
        y.append(ty)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    #ax.plot(x, y, linestyle="", marker=".", color=c1)
    ax.plot(x, y, color=c1)
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
