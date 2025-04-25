from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def hsv2rgb(h: float=0.0, s: float=1.0, v: float=1.0) -> str:
    rgb: np.ndarray = (255 * ((np.clip(np.abs(np.modf(h + np.array([0.0, 2.0, 1.0]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).round(0).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    rng: np.random.Generator = np.random.default_rng()
    offset: float = rng.random()
    saturation: float = 0.1
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    hue: float = offset + 0.5
    n: int = 1+100
    a: float
    th: float
    c: float
    s: float
    t: np.ndarray = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    cos: np.ndarray = np.cos(t)
    sin: np.ndarray = np.sin(t)
    x: np.ndarray
    y: np.ndarray
    for i in range(n):
        saturation = 0.8 - 0.6 * i/(n-1)
        color: str = hsv2rgb(hue, saturation, value)
        a = rng.random()
        th = rng.random() * np.pi
        c = np.cos(th)
        s = np.sin(th)
        x, y = np.array([[c, -s], [s, c]]) @ np.array([cos, a*sin])
        ax.plot(x, y, linewidth=2, color=color)
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
