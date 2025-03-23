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
    t: np.ndarray = np.linspace(0, 2*np.pi, 1+10000, endpoint=True)
    n: int = 8
    for i in range(1, n+1):
        r: np.ndarray = 1 - i/n * np.cos(13*t+2*np.pi*i/n)
        x: np.ndarray = r * np.sin(t)
        y: np.ndarray = r * np.cos(t)
        ax.plot(x, y, color=c1, linewidth=3)
    #ax.set_xlim(0, 2*np.pi)
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
