from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    # start
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#008B52"
    c1: str = "#412554"
    c2: str = "#FFE4A8"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    n: int = 192
    t: np.ndarray = np.linspace(0, np.pi, 1+3600, endpoint=True)
    col: list[str] = [c1, c2]
    for i in range(n):
        r: np.ndarray = np.exp(np.sin(t)) - 2*np.cos(4*t) + np.pow(np.sin((4*t-np.pi)/24), 5)
        ax.plot(r*np.cos(t), r*np.sin(t), color=col[i%2], linewidth=6)
        t += np.pi
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
