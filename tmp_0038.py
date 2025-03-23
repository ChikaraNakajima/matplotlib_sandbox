from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    # start
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#DB7307"
    c1: str = "#64DB8F"
    c2: str = "#F9F790"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray
    x: np.ndarray
    y: np.ndarray
    t = np.linspace(0, 6*np.pi, 8, endpoint=True)
    for i in range(16):
        for j in range(9):
            y = -0.25*np.cos(t+np.pi/14*(i+j))
            x = -0.25*np.sin(t+np.pi/14*(i+j))
            ax.plot(x+i, y+j, color=c1, linewidth=2)
    t = np.linspace(0, 4*np.pi, 8, endpoint=True)
    for i in range(15):
        for j in range(8):
            y = -0.25*np.cos(t+np.pi/14*(i+j))
            x = -0.25*np.sin(t+np.pi/14*(i+j))
            ax.plot(x+i+0.5, y+j+0.5, color=c2, linewidth=2)
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
