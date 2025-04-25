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
    bgc: str = hsv2rgb(0.625, 0.75, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    k: int = 0
    for i in range(16):
        for j in range(9):
            n: int = 1 + j
            t: np.ndarray = np.linspace(0, n*2*np.pi, 1+n*3600, endpoint=True)
            r: np.ndarray = 1 + np.cos(t*(1+i)/n) * np.sin(t*(1+i)/n)
            r *= 0.3
            x: np.ndarray = r * np.cos(t)
            y: np.ndarray = r * np.sin(t)
            ax.plot(x+i, y+j, linewidth=2, color=hsv2rgb(k/288, 0.5, 1))
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
