from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def hsv2rgb(h: float, s: float, v: float) -> str:
    rgb: np.ndarray = np.round(255 * ((np.clip(np.abs(np.modf(h + np.array([0.0, 2.0, 1.0]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    rng: np.random.Generator = np.random.default_rng()
    offset: float = rng.random()
    saturation: float = 0.5
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    x: float = -0.72
    y: float = -0.64
    xn: float
    yn: float
    xl: list[float] = [x]
    yl: list[float] = [y]
    a: float = 0.9
    b: float = -0.6013
    c: float = 2.0
    d: float = 0.5
    for i in range(2**18):
        xn = x*x - y*y + a*x + b*y
        yn = 2*x*y + c*x + d*y
        x = xn
        y = yn
        xl.append(x)
        yl.append(y)
    xa: np.ndarray = np.array(xl)
    ya: np.ndarray = np.array(yl)
    xmax: float = xa.max()
    xmin: float = xa.min()
    ymax: float = ya.max()
    ymin: float = ya.min()
    l: float = max(xmax-xmin, ymax-ymin)
    xa = (xa-xmin)/l
    ya = (ya-ymin)/l
    k: int = 0
    for i in range(3):
        for j in range(2):
            ax.plot(xa+i, ya+j, linestyle="", marker="o", color=hsv2rgb(offset+0.5+(k-2.5)/12, saturation, value))
            k += 1
    # arrange
    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(bgc)
    fig.set_facecolor(bgc)
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
