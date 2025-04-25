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
    l: float = 2
    n: int = 12
    col: list[str] = [c1, c2]
    t: np.ndarray = np.linspace(-l, l, 10001, endpoint=True)
    x = np.cosh(t)
    y = np.sinh(t)
    for i in range(1, 1+n, 1):
        c: str = col[i%2]
        ax.plot(x, y*i/n, color=c)
        ax.plot(-x, y*i/n, color=c)
        ax.plot(y*i/n, x, color=c)
        ax.plot(y*i/n, -x, color=c)
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
