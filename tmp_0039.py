from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    # start
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#ff6347"
    c1: str = "#fffacd"
    c2: str = "#a52a2a"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    r: float = 0.4
    t: np.ndarray = np.linspace(0, 4*np.pi, 8, endpoint=True)
    y0: np.ndarray = r*np.cos(t)
    x0: np.ndarray = r*np.sin(t)
    t: np.ndarray = np.linspace(0, 6*np.pi, 8, endpoint=True)
    y1: np.ndarray = r*np.cos(t)
    x1: np.ndarray = r*np.sin(t)
    col: list[str] = [c2, c1]
    for i in range(18):
        if i%2:
            x: np.ndarray = x0
            y: np.ndarray = y0
        else:
            x: np.ndarray = x1
            y: np.ndarray = y1
        for j in range(10):
            c: str = col[j%2]
            ud: int = (2*(j%2)-1)
            j -= 0.5 if i%2 else 0
            ax.plot(x+i, ud*y+j, color=c, linewidth=2)
    # finish
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(c0)
    fig.set_facecolor(c0)
    fig.tight_layout()
    fig.savefig(fp, facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
