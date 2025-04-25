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
    bgc: str = hsv2rgb(0.75, 0.5, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    n: int = 72
    r = 0.04
    t: np.ndarray = np.linspace(0, 2*np.pi, 5, endpoint=False)
    t += np.pi/5
    c: list[float] = np.cos(t).tolist()
    s: list[float] = np.sin(t).tolist()
    for i in range(n+1):
        ax.plot(c+[c[0]], s+[s[0]], linewidth=6, color=hsv2rgb(0.25 + 0.25*(i-n/2)/n, 0.5, 1))
        c = [r*c[j]+(1-r)*c[(1+j)%len(c)] for j in range(len(c))]
        s = [r*s[j]+(1-r)*s[(1+j)%len(s)] for j in range(len(s))]
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
