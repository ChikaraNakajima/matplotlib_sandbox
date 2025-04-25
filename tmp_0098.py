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
    saturation: float = 0.5
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    n: int = 360
    m0: int = 5
    m1: int = 2
    r: float = m1 / m0
    t: np.ndarray = np.linspace(0, m1*2*np.pi, m1*360, endpoint=False).tolist()
    x0: float
    y0: float
    x1: float
    y1: float
    for i, th in enumerate(t):
        x0 = (1-r)*np.sin(th) - r*np.sin((1/r-1)*th)
        y0 = (1-r)*np.cos(th) + r*np.cos((1/r-1)*th)
        th += 0.5*np.pi
        x1 = (1-r)*np.sin(th) - r*np.sin((1/r-1)*th)
        y1 = (1-r)*np.cos(th) + r*np.cos((1/r-1)*th)
        hue: float = offset + 0.75 + (i-len(t)/2+0.5)/len(t)*0.25
        ax.plot([x0, x1], [y0, y1], linewidth=6, color=hsv2rgb(hue, saturation, value))
    n: int = 360
    m0: int = 5
    m1: int = 1
    r: float = m1 / m0
    t: np.ndarray = np.linspace(0, m1*2*np.pi, m1*360, endpoint=False).tolist()
    for i, th in enumerate(t):
        x0 = (1-r)*np.sin(th) - r*np.sin((1/r-1)*th)
        y0 = (1-r)*np.cos(th) + r*np.cos((1/r-1)*th)
        th += 0.5*np.pi
        x1 = (1-r)*np.sin(th) - r*np.sin((1/r-1)*th)
        y1 = (1-r)*np.cos(th) + r*np.cos((1/r-1)*th)
        hue: float = offset + 0.25 + (i-len(t)/2+0.5)/len(t)*0.25
        ax.plot([x0+2, x1+2], [y0, y1], linewidth=6, color=hsv2rgb(hue, saturation, value))
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
