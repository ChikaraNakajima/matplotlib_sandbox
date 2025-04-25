from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class RandomWalk:
    def __init__(self, position: tuple[int, int]=(0, 0), flag: bool=True) -> None:
        self.position: tuple[int, int] = position
        self.flag: bool = flag
        self.xl: list[int] = [position[0]]
        self.yl: list[int] = [position[1]]
        return None

    def add(self) -> None:
        self.xl.append(self.position[0])
        self.yl.append(self.position[1])
        return None


def hsv2rgb(h: float, s: float, v: float) -> str:
    rgb: np.ndarray = np.round(255 * ((np.clip(np.abs(np.modf(h + np.array([0, 2, 1]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    bgc: str = hsv2rgb(0.6, 1, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    vl: list[list[int]] = [
        [ 1,  0],
        [ 0,  1],
        [-1,  0],
        [ 0, -1],
    ]
    rng: np.random.Generator = np.random.default_rng()
    points: list[RandomWalk] = []
    fa: set[tuple[int, int]] = set()
    while True:
        p: tuple[int, int] = tuple(rng.integers(0, 128, size=2).tolist())
        if p not in fa:
            points.append(RandomWalk(p))
            fa.add(p)
        else:
            continue
        if 255 < len(fa):
            break
    for i in range(2**64):
        for p in points:
            if not p.flag:
                continue
            o: int = rng.integers(0, 4)
            for i in range(4):
                x: int
                y: int
                x, y = vl[(o+i)%4]
                xy: tuple[int, int] = (p.position[0]+x, p.position[1]+y)
                if xy not in fa:
                    fa.add(xy)
                    p.position = xy
                    p.add()
                    break
                else:
                    continue
            else:
                p.flag = False
        if not any(p.flag for p in points):
            break
    for i, p in enumerate(points):
        ax.plot(p.xl, p.yl, linewidth=3, color=hsv2rgb(i/128, 0.5, 1))
    # arrange
    #ax.set_xlim(0, 1)
    #ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(bgc)
    fig.set_facecolor(bgc)
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
