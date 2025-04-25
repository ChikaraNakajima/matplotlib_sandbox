from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色バリエーション BOOK 2
    colors: list[str] = [
        f"#{r:02x}{g:02x}{b:02x}"
        for r, g, b in [
            (200, 219, 128),
            (216, 184, 214),
            (83, 179, 129),
            (147, 195, 233),
            (158, 162, 78),
            (253, 251, 213),
            (165, 189, 226),
            (198, 230, 229),
            (59, 163, 203),
            (98, 190, 192),
        ]
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    r: float = 0.4
    t: np.ndarray = np.linspace(0, 4*np.pi, 6, endpoint=True)
    base: np.array = r * np.array([np.sin(t), np.cos(t)])
    for i in range(5):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    th: float = (3*i+k+3*j+l)/10*np.pi
                    c: float = np.cos(th)
                    s: float = np.sin(th)
                    m: np.ndarray = np.array([[c, -s], [s, c]])
                    p: np.ndarray = m @ base
                    ax.plot(p[0]+3*i+k, p[1]+3*j+l, linewidth=8, color=colors[3*k+l])
    # arrange
    #ax.set_xlim(-1, 11)
    #ax.set_ylim(-2, 6)
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
