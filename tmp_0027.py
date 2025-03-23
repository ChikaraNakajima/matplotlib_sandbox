import shutil
import multiprocessing
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(n: int) -> None:
    dp: Path = Path(__file__).resolve().with_suffix("")
    fp: Path = dp.joinpath(f"{n:04d}.png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    r: float = n/360
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi, 5, endpoint=False)
    c: np.ndarray = np.sin(t)
    s: np.ndarray = np.cos(t)
    th: float = r * 0.4*np.pi
    c, s = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]) @ np.array([c, s])
    ax.plot(c.tolist()+[c[0]], s.tolist()+[s[0]], color=c1, linewidth=3)
    for i in range(64):
        c = r * c + (1-r) * np.roll(c, 1)
        s = r * s + (1-r) * np.roll(s, 1)
        ax.plot(c.tolist()+[c[0]], s.tolist()+[s[0]], color=c1, linewidth=3)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
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
