from pathlib import Path

import numpy as np

from template_plt import plt


def main() -> None:
    x: np.ndarray = np.linspace(-np.pi, np.pi, 10001, endpoint=True)
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    w: float = 0.5
    for i in range(9):
        y: np.ndarray = np.sin(x*w) / w
        w *= 2
        ax.plot(x, y, color="#E06B22")
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor("#29292E")
    fig.set_facecolor("#29292E")
    fig.tight_layout()
    fig.savefig(Path(__file__).resolve().with_suffix(".png"), facecolor=fig.get_facecolor())
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
