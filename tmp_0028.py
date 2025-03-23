import shutil
import multiprocessing
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(n: int) -> None:
    dp: Path = Path(__file__).resolve().with_suffix("")
    fp: Path = dp.joinpath(f"{n:04d}.png")
    c0: str = "#E64E00"
    c1: str = "#E6EB00"
    c2: str = "#65B48E"
    c3: str = "#3E5CC5"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    t0: float = 2*np.pi * n/360
    t: np.ndarray = t0 + np.linspace(-1.5*np.pi, 1.5*np.pi, 10001, endpoint=True)
    ax.plot(t0+np.cos(t), 1+np.sin(t), color=c2, linewidth=3)
    ax.plot([t0, t0-np.sin(t0)], [1, 1-np.cos(t0)], color=c2, linewidth=3)
    ax.plot([t[0], t[-1]], [0, 0], color=c2, linewidth=3)
    a: int = 16
    for i in range(1, a+1):
        r: float = i/a
        x: np.ndarray = t - r*np.sin(t)
        y: np.ndarray = 1 - r*np.cos(t)
        ax.plot(x, y, color=c1, linewidth=3)
    mx: list[float] = [t0-i/a*np.sin(t0) for i in range(a+1)]
    my: list[float] = [1-i/a*np.cos(t0) for i in range(a+1)]
    ax.plot(mx, my, color=c3, marker="o", linestyle="")
    ax.set_xlim(t0-np.pi, t0+np.pi)
    ax.set_ylim(-0.05, 2.05)
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
