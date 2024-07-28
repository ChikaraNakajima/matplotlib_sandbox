import shutil
import multiprocessing
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(data: dict) -> None:
    num: int = data["i"]
    dp: Path = data["dp"]
    x: np.ndarray = np.linspace(-np.pi, np.pi, 10001, endpoint=True)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    w: int = 1
    for i in range(8):
        y: np.ndarray = np.sin((x+2.0*np.pi/360.0*num)*w) / w
        w *= 2
        ax.plot(x, y, color="#E06B22")
    ax.axis("off")
    #ax.set_xlim(-np.pi, np.pi)
    #ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")
    ax.set_facecolor("#29292E")
    fig.set_facecolor("#29292E")
    fig.tight_layout()
    fig.savefig(dp.joinpath(f"{num:04d}.png"), facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


def main() -> None:
    home: Path = Path(__file__).resolve().parent
    dp: Path = Path(__file__).resolve().with_suffix("")
    if dp.is_dir():
        shutil.rmtree(dp)
    dp.mkdir()
    data = [{"i": i, "dp": dp} for i in range(360)]
    with multiprocessing.Pool(multiprocessing.cpu_count()//2) as p:
        for i in p.imap_unordered(make_graph, data):
            pass
    return None


if __name__ == "__main__":
    main()
