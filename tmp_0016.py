import multiprocessing
import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(n: int) -> None:
    dp: Path = Path(__file__).resolve().with_suffix("")
    fp: Path = dp.joinpath(f"{n:04d}.png")

    c0: str = "#96743B"
    c1: str = "#4D3400"
    c2: str = "#E5DBB5"
    c3: str = "#601F1C"
    c4: str = "#795840"
    c5: str = "#2A5249"
    c6: str = "#192200"
    c7: str = "#AEAB92"
    c8: str = "#3E1900"

    lw: float = 12

    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()

    ax.plot([-100, 100], [0, 0], color=c1, linewidth=lw)
    ax.plot([0, 0], [-100, 100], color=c2, linewidth=lw)

    d: float = n/360 * 2.0*np.pi
    dc: float = np.cos(d)
    ds: float = np.sin(d)

    t: np.ndarray = np.linspace(-2.0*np.pi, 2.0*np.pi, 10001, endpoint=True)
    c: np.ndarray = np.cos(t+d)
    s: np.ndarray = np.sin(t+d)

    ax.plot(c, s, color=c3, linewidth=lw)

    ax.plot(t, s, color=c7, linewidth=lw)
    ax.plot(c, t, color=c8, linewidth=lw)

    ax.plot([0, dc], [ds, ds], color=c5, linewidth=lw)
    ax.plot([dc, dc], [0, ds], color=c6, linewidth=lw)
    ax.plot([0, 100*dc], [0, 100*ds], color=c4, linewidth=lw)

    ax.axis("off")
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-1.2, 1.2)
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
