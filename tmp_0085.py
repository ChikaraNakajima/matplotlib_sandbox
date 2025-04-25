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
    bgc: str = hsv2rgb(0.25, 0.75, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    l: int = 0
    t: np.ndarray = np.linspace(0, 2*np.pi, 4, endpoint=True)
    for i in range(16):
        for j in range(9):
            for k in range(3):
                c: np.ndarray = 0.4 * np.cos(t+k/12*np.pi+l/12*np.pi)
                s: np.ndarray = 0.4 * np.sin(t+k/12*np.pi+l/12*np.pi)
                ax.plot(i+c, j+s, linewidth=3, color=hsv2rgb(0.5+k/24+l/288, 0.5, 1))
            l += 1
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
