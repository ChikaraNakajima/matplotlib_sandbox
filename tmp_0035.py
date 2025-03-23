from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#008B52"
    c1: str = "#412554"
    c2: str = "#FFE4A8"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    t: np.ndarray = np.linspace(-np.pi, np.pi, 1+10000, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    v0: float = 32
    v1: float = 16
    n: int = 24
    col: list[str] = [c1, c2]
    for i in range(n):
        r: float = (n-i)*v0
        ax.plot(r*c+i*v1, r*s, color=col[i%2], linewidth=4)
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
