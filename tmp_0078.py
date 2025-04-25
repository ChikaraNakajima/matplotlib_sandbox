from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def hsv2rgb(h: float, s: float, v: float) -> str:
    rgb: np.ndarray = np.round(255 * ((np.clip(np.abs(np.modf(h + np.array([0, 2, 1]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    bgc: str = hsv2rgb(0.5, 0.75, 1)
    c0: str = hsv2rgb(0.1, 0.5, 1)
    c1: str = hsv2rgb(0.9, 0.5, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 3601, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for x in range(3):
        for y in range(2):
            for i in range(6):
                r: float = (1+i)/6
                ax.plot(2.4*x+r*c, 2.4*y+r*s, color=c0, linewidth=12)
            n0: int = 12
            n1: int = 6
            for i in range(n0):
                for j in range(1, 1+n1):
                    l: float = j/n1
                    r0: float = 0.125 * l
                    th: float = 2*np.pi * i/n0 + 1/3 * np.pi * l
                    ax.plot(2.4*x+r0*c+l*np.cos(th), 2.4*y+r0*s+l*np.sin(th), color=c1, linewidth=12)
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
