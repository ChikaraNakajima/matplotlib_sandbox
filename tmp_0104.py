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
    t: np.ndarray = np.linspace(0, 2*np.pi, 5, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    hue: float = offset + 0.4
    color: str = hsv2rgb(hue, saturation, value)
    r: float
    for i in range(16):
        for j in range(9):
            for k in range(4):
                r = 0.5 * (1+k)*0.2
                ax.plot(r*c+i, r*s+j, linewidth=2, color=color)
    hue = offset + 0.5
    color = hsv2rgb(hue, saturation, value)
    for i in range(16):
        for j in range(9):
            ax.plot(0.5*c+i, 0.5*s+j, linewidth=6, color=color)
    hue = offset + 0.6
    color = hsv2rgb(hue, saturation, value)
    for i in range(15):
        for j in range(8):
            for k in range(4):
                r = 0.5 * (1+k)*0.2
                ax.plot(r*c+i+0.5, r*s+j+0.5, linewidth=2, color=color)
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
