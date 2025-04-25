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
    px: np.ndarray = np.array([0.0])
    py: np.ndarray = np.array([0.0])
    hx: np.ndarray = np.cos(np.linspace(0, 2*np.pi, 6, endpoint=False))
    hy: np.ndarray = np.sin(np.linspace(0, 2*np.pi, 6, endpoint=False))
    px = np.concatenate([px, hx])
    py = np.concatenate([py, hy])
    hx *= 2.0
    hy *= 2.0
    px = np.concatenate([px, hx])
    py = np.concatenate([py, hy])
    hx = np.array([0.5*(hx[i]+hx[(1+i)%6]) for i in range(6)])
    hy = np.array([0.5*(hy[i]+hy[(1+i)%6]) for i in range(6)])
    px = np.concatenate([px, hx])
    py = np.concatenate([py, hy])
    n: int = 360
    t: np.ndarray = np.linspace(0, 2*np.pi, 1+3600, endpoint=True)
    for i in range(1+n):
        r: np.ndarray = 1 + i/n * np.cos(6*t+i/n*2*np.pi)
        r *= 0.2
        x: np.ndarray = r * np.cos(t)
        y: np.ndarray = r * np.sin(t)
        for j, (cx, cy) in enumerate(zip(px, py)):
            hue: float = offset + 0.5 + (i/n-0.5)*0.25 + (j-0.5*len(px)+0.5)/len(px)*0.25
            ax.plot(cx+x, cy+y, linewidth=2, color=hsv2rgb(hue, saturation, value))
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
