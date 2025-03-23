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
    v0: list[float] = [1, 0]
    v1: list[float] = [0.5, np.sqrt(3)*0.5]
    n: int = 4
    col: list[str] = [c1, c2]
    for k in range(1, 1+n):
        for i in range(16):
            for j in range(16):
                cx: float = i*v0[0] + j*v1[0]
                cy: float = i*v0[1] + j*v1[1]
                ax.plot(k/n*c+cx, k/n*s+cy, color=col[k%2], linewidth=4)
    ax.set_xlim(4, 12)
    ax.set_ylim(2, 6.5)
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
