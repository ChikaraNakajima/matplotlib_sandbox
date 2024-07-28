import multiprocessing
import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(n: int) -> None:
    dp: Path = Path(__file__).resolve().with_suffix("")
    fp: Path = dp.joinpath(f"{n:04d}.png")

    c0: str = "#192200"
    c1: str = "#96743B"
    c2: str = "#E5DBB5"

    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()

    d: float
    r: float
    y: np.ndarray
    x: np.ndarray

    t: np.ndarray = np.linspace(0.0, 2.0*np.pi, 6, endpoint=True)
    t += n/360 * 2.0*np.pi
    r = 0.2

    for i in range(16):
        for j in range(9):
            d = (i+j) * 0.1*np.pi
            y = r * np.cos(t+d)
            x = r * np.sin(t+d)
            ax.plot(x+i, y+j, color=c1)

    t = np.linspace(0.0, 4.0*np.pi, 6, endpoint=True)
    t -= n/360 * 2.0*np.pi
    r = 0.25

    for i in range(15):
        for j in range(8):
            d = (i+j) * 0.1*np.pi
            y = r * np.cos(t+d)
            x = r * np.sin(t+d)
            ax.plot(x+i+0.5, y+j+0.5, color=c2)

    ax.axis("off")
    ax.set_xlim(-0.5, 15.5)
    ax.set_ylim(-0.5, 8.5)
    ax.set_aspect("equal")
    ax.set_facecolor(c0)
    fig.set_facecolor(c0)
    fig.tight_layout()
    fig.savefig(fp, facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


def main() -> None:
    dp: Path = Path(__file__).resolve().with_suffix("")
    if dp.is_dir():
        shutil.rmtree(dp)
    dp.mkdir()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        for i in p.imap_unordered(make_graph, range(360)):
            pass
    return None


if __name__ == "__main__":
    main()
