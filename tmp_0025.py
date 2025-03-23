from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi, 10001, endpoint=True)
    x: np.ndarray = np.cos(t)
    y: np.ndarray = np.sin(t)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    px: np.ndarray
    py: np.ndarray
    n: int = 32
    for i in range(1, n+1):
        c: np.float64 = np.cos(np.pi*i/n)
        s: np.float64 = np.sin(np.pi*i/n)
        px, py = np.array([[c, -s], [s, c]]) @ np.array([x, y*i/n])
        ax.plot(px, py, color=c1, linewidth=3)
    #ax.plot([-1.0, 1.0], [0.0, 0.0], color=c1, linewidth=3)
    #ax.set_xlim(-0.05, 9.05)
    #ax.set_ylim(-0.05, 9.05)
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
