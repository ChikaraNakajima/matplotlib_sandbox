from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def hsv2rgb(h: float=0.0, s: float=1.0, v: float=1.0) -> str:
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
    pn: list[list[int]] = [
        [i, j]
        for i in [3, 5, 7, 11]
        for j in range(1, 1+i//2)
    ]
    # plot
    r: float = 0.4
    l: float = 0.45
    lx: np.ndarray = np.array([l, l, -l, -l, l])
    ly: np.ndarray = np.array([l, -l, -l, l, l])
    for i in range(16):
        for j in range(9):
            n: int
            m: int
            n, m = rng.choice(pn)
            t: np.ndarray = np.linspace(0, m*2*np.pi, 1+n, endpoint=True)
            t += 2*np.pi * rng.random()
            x: np.ndarray = r * np.cos(t)
            y: np.ndarray = r * np.sin(t)
            hue: float = offset + 0.25 + 0.5 * rng.random()
            ax.plot(x+i, y+j, linewidth=2, color=hsv2rgb(hue, saturation, value))
            hue: float = offset + 0.25 + 0.5 * rng.random()
            ax.plot(lx+i, ly+j, linewidth=2, color=hsv2rgb(hue, saturation, value))
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
