import math
import random
from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    n: int = 7
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi*n, 10001, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    for i in range(1, n//2+1):
        r: float = i/n
        x: np.ndarray = (1-r)*s - r*np.sin((1/r-1)*t)
        y: np.ndarray = (1-r)*c + r*np.cos((1/r-1)*t)
        y *= -1
        ax.plot(x, y, color=c1)
    for i in range(1, n):
        r = i/n
        x = (1+r)*s - r*np.sin((1/r+1)*t)
        y = (1+r)*c - r*np.cos((1/r+1)*t)
        y *= -1
        ax.plot(x, y, color=c1)
    ax.plot(c, s, color=c1)
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
