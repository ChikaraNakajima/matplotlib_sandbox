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
    t: np.ndarray = 4*np.linspace(-np.pi, np.pi, 1+10000, endpoint=True)
    y: np.ndarray = np.sin(t)
    n: int = 16
    for i in range(n):
        th: float = i/n * np.pi
        px: np.ndarray
        py: np.ndarray
        px, py = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]]) @ np.array([t, y])
        ax.plot(px, py, color=c1, linewidth=3)
    #ax.set_xlim(-np.pi, np.pi)
    #ax.set_ylim(0, 1)
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
