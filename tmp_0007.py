import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


def make_graph(dp: Path, n0: int, n1: int) -> None:
    fp: Path = dp.joinpath(f"{n0}_{n1}.png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi*n0, 100001, endpoint=True)
    r: np.ndarray = np.sin(t*n1/n0)
    x: np.ndarray = np.cos(t) * r
    y: np.ndarray = np.sin(t) * r
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=6, color=c1)
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
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            else:
                make_graph(dp, i, j)
    return None


if __name__ == "__main__":
    main()
