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
    colors: list[str] = [hsv2rgb(i/3+1/6, 0.5, 1) for i in range(3)]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    m: int = 7
    l: float = 0.4
    t: np.ndarray
    x: np.ndarray
    y: np.ndarray
    for i in range(1, 1+m//2):
        t = np.linspace(0, 2*np.pi*i, 1+3600*i, endpoint=True)
        r: float = i/m
        y = (1-r) * np.cos(t) + r * np.cos((1/r-1)*t)
        x = (1-r) * np.sin(t) - r * np.sin((1/r-1)*t)
        for j in range(3):
            for k in range(2):
                pm: int = 2*((j+k)%2)-1
                ax.plot(l*x+j, pm*l*y+k, linewidth=6, color=colors[0])
    t = np.linspace(0, 2*np.pi*i, 1+3600, endpoint=True)
    x = np.cos(t)
    y = np.sin(t)
    for j in range(3):
        for k in range(2):
            ax.plot(l*x+j, l*y+k, linewidth=6, color=colors[1])
    # arrange
    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(colors[-1])
    fig.set_facecolor(colors[-1])
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
