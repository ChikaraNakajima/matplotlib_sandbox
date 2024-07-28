import multiprocessing
import shutil
from pathlib import Path

import numpy as np

from template_plt import plt


# 180 frame (6 s) で 1 周する。
# 7 周する。
# 180 * 7 = 1260 frame
num: int = 11
width = 6
colors = [
    [244, 158, 38],

    [178, 47, 65],
    [236, 109, 127],
    [243, 158, 110],
    [152, 80, 152],
    [188, 34, 35],

    [225, 50, 39],
    [213, 182, 50],
    [130, 161, 42],
    [240, 225, 135],
    [251, 240, 209],

    [238, 164, 177],
    [253, 206, 43],
    [245, 164, 0],
    [156, 175, 72],
    [39, 69, 115],

    [138, 43, 42],
    [202, 67, 75],
    [191, 197, 86],
    [244, 157, 63],
    [76, 41, 76],

    [92, 29, 57],
    [231, 94, 21],
    [173, 27, 70],
    [88, 103, 50]
]

colors = [f"#{i:02X}{j:02X}{k:02X}" for i, j, k in colors]


def make_graph(data: dict) -> None:
    n: int = data["n"]
    dp: Path = data["dp"]
    fp: Path = dp.joinpath(f"{n:04d}.png")

    delta: float = n / 180 * 2.0*np.pi

    t: np.ndarray = np.linspace(0.0, delta, 1+2*n*10, endpoint=True)

    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()

    cindex: int = 0

    for i in range(1, num//2+1):
        rm: float = i/num
        y: np.ndarray = (1.0-rm)*np.cos(t) + rm*np.cos((1.0/rm-1.0)*t)
        x: np.ndarray = (1.0-rm)*np.sin(t) - rm*np.sin((1.0/rm-1.0)*t)
        ax.plot(x, y, color=colors[cindex], linewidth=width)
        cindex += 1

    tr: np.ndarray = np.linspace(0.0, 2.0*np.pi, 10001, endpoint=True)
    cr: np.ndarray = np.cos(tr)
    sr: np.ndarray = np.sin(tr)
    for i in range(1, num//2+1):
        rm = i/num
        y = (1.0-rm)*np.cos(t[-1]) + rm*cr
        x = (1.0-rm)*np.sin(t[-1]) + rm*sr
        ax.plot(x, y, color=colors[cindex], linewidth=width)
        cindex += 1

    for i in range(1, num//2+1):
        rm = i/num
        y: np.ndarray = (1.0-rm)*np.cos(t[-1]) + rm*np.cos((1.0/rm-1.0)*t[-1])
        x: np.ndarray = (1.0-rm)*np.sin(t[-1]) - rm*np.sin((1.0/rm-1.0)*t[-1])
        ax.plot(x, y, linestyle="", marker="o", color=colors[cindex], markersize=12)
        cindex += 1

    ax.plot(cr, sr, color=colors[cindex], linewidth=width)
    cindex += 1

    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(colors[cindex])
    fig.set_facecolor(colors[cindex])
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

    data = [{"n": i, "dp": dp} for i in range(num*180)]
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        for i in p.imap_unordered(make_graph, data):
            pass
    return None


if __name__ == "__main__":
    main()
