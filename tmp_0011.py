from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    c0: str = "#F1E7A3"
    c1: str = "#E89434"
    c2: str = "#A1B93C"
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    n: int = 7
    t: np.ndarray = np.linspace(0.0, 2.0*np.pi*n, 10001, endpoint=True)
    c: np.ndarray = np.cos(t)
    s: np.ndarray = np.sin(t)
    for i in range(1, n):
        rm: float = i / n
        mc: np.ndarray = np.cos((1.0/rm-1.0)*t)
        ms: np.ndarray = np.sin((1.0/rm-1.0)*t)
        for j in range(1, n):
            rd: float = j / n
            y: np.ndarray = (1.0-rm)*c + rd * mc
            x: np.ndarray = (1.0-rm)*s - rd * ms
            y *= -1
            ax.plot(c+3.6*i, s+3.6*j, color=c2)
            ax.plot(x+3.6*i, y+3.6*j, color=c1)
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
