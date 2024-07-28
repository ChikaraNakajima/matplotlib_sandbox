from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#29292E"
    c1: str = "#E06B22"
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi, 10001, endpoint=True)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    for i in range(1, 10):
        c: np.ndarray = np.cos(t*i)
        for j in range(1, 10):
            s: np.ndarray = np.sin(t*j)
            ax.plot(c+2.5*i, s+2.5*j, color=c1)
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
