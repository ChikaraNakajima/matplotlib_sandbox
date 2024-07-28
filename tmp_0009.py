import multiprocessing
import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(data: dict) -> None:
    dp: Path = data["dp"]
    n: int = data["n"]
    fp: Path = dp.joinpath(f"{n:04d}.png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    for i in range(1, 10):
        t: np.ndarray = np.linspace(0.0, 2.0*np.pi*i, 10001, endpoint=True)
        for j in range(1, 10):
            d: int = 1 if (i+j) % 2 else -1
            r: np.ndarray = np.sin(t*j/i)
            x: np.ndarray = np.cos(t) * r
            y: np.ndarray = np.sin(t) * r
            th: float = 2.0 * np.pi * n / 360 * d
            c: float = np.cos(th)
            s: float = np.sin(th)
            x, y = np.array([[c, -s], [s, c]]) @ np.array([x, y])
            ax.plot(x+2.5*i, y+2.5*j, color=c1)
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
    data = [
        {"dp": dp, "n": i}
        for i in range(360)
    ]
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        for i in p.imap_unordered(make_graph, data):
            pass
    return None


if __name__ == "__main__":
    main()
