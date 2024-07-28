import math
import random
from pathlib import Path

from template_plt import plt


def random_walk(x: float, y: float) -> tuple[float, float]:
    r: int = int(8.0*random.random())
    if r == 0:
        x += 1
    elif r == 1:
        x += 1
        y += 1
    elif r == 2:
        y += 1
    elif r == 3:
        x -= 1
        y += 1
    elif r == 4:
        x -= 1
    elif r == 5:
        x -= 1
        y -= 1
    elif r == 6:
        y -= 1
    elif r == 7:
        x += 1
        y -= 1
    return x, y


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    x: list[float] = [0]
    y: list[float] = [0]
    for i in range(100000):
        tx, ty = random_walk(x[-1], y[-1])
        x.append(tx)
        y.append(ty)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
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
