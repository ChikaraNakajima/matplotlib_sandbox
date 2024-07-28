from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi*19, 100001, endpoint=True)
    x: np.ndarray = np.cos(t) * np.sin(t*7/19)
    y: np.ndarray = np.sin(t) * np.sin(t*-8/19)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=6, color=c1)
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
