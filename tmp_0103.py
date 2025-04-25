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
    saturation: float = 0.6
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    value -= 0.2
    t: np.ndarray = np.linspace(0, 2*np.pi, 1+180, endpoint=True) + np.pi*0.25
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    top: np.ndarray = np.array([max(i, j) for i, j in zip(c, s)])
    bottom: np.ndarray = np.array([min(i, j) for i, j in zip(c, s)])
    hue: float = offset + 0.4
    color: str = hsv2rgb(hue, saturation, value)
    ax.stem(t, top      , bottom= 1.3, linefmt=color, markerfmt=color, basefmt=color)
    ax.stem(t, bottom   , bottom=-1.3, linefmt=color, markerfmt=color, basefmt=color)
    base: np.ndarray = 0.5*(top+bottom)
    hue = offset + 0.5
    color = hsv2rgb(hue, saturation, value)
    ax.plot(t, base, linewidth=2, color=color)
    hue = offset + 0.6
    color = hsv2rgb(hue, saturation, value)
    for l, i, j, k in zip(t, base, top, bottom):
        ax.stem(l, j, bottom=i, linefmt=color, markerfmt=color, basefmt=color)
        ax.stem(l, k, bottom=i, linefmt=color, markerfmt=color, basefmt=color)
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
