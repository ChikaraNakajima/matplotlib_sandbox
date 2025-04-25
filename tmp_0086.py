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
    bgc: str = hsv2rgb(0.2, 1, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    vl: np.ndarray = np.array([
        [ 1,  0],
        [ 0, -1],
        [-1,  0],
        [ 0,  1],
    ])
    p0: np.ndarray = np.array([0, 0])
    p1: np.ndarray
    l: int = 1
    x: list[int] = [p0[0]]
    y: list[int] = [p0[1]]
    for i in range(16):
        p1 = p0 + l * vl[i%4]
        x.append(p1[0])
        y.append(p1[1])
        p0 = p1
        l += 1
    xy: np.ndarray = np.array([x, y]) *0.05
    k: int = 0
    ml: np.ndarray = np.array([
        [
            [np.cos(i*0.5*np.pi), -np.sin(i*0.5*np.pi)],
            [np.sin(i*0.5*np.pi),  np.cos(i*0.5*np.pi)],
        ]
        for i in range(4)
    ])
    px: np.ndarray
    py: np.ndarray
    for i in range(16):
        for j in range(9):
            px, py = ml[k%4] @ xy
            ax.plot(px+i, py+j, linewidth=3, color=hsv2rgb(1, 1, 1))
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
