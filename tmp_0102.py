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
    saturation: float = 0.0
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    saturation = 0.5
    n: int = 1000
    m: int = 5
    t: np.ndarray = np.linspace(0, 2*np.pi, m, endpoint=False)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    k: int = 0
    for i in range(m):
        sx: float = s[i]
        ex: float = s[i-1]
        sy: float = c[i]
        ey: float = c[i-1]
        for j in range(n):
            r: float = j/n
            x: float = r*sx + (1-r)*ex
            y: float = r*sy + (1-r)*ey
            hue: float = offset + 0.5 + (k-0.5*m*n+0.5)/(m*n)
            ax.plot([0, x], [0, y], linewidth=1, color=hsv2rgb(hue, saturation, value))
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
