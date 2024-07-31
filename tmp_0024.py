from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    lx: np.ndarray = np.linspace(0, 9, 10, endpoint=True)
    ly: np.ndarray = np.linspace(0, 9, 10, endpoint=True)
    xx, yy = np.meshgrid(lx, ly)
    ax.plot(xx, yy, color=c1, linewidth=12)
    ax.plot(yy, xx, color=c1, linewidth=12)
    ax.set_xlim(-0.05, 9.05)
    ax.set_ylim(-0.05, 9.05)
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
