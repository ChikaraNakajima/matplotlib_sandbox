from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class RandomWalk:
    def __init__(
        self,
        position: np.ndarray,
        velocity: np.ndarray,
        velocity_k: float=0.1,
        angle_k: float=np.pi/6,
        velocity_limit: float=1.0,
    ) -> None:
        self.position: np.ndarray = position
        self.velocity: np.ndarray = position
        self.velocity_k: float = velocity_k
        self.angle_k: float = angle_k
        self.velocity_limit: float = velocity_limit

        self.lx: list[float] = [position[0]]
        self.ly: list[float] = [position[1]]
        return None

    def update_velocity(self, rng: np.random.Generator) -> None:
        a: float = np.arctan2(self.velocity[1], self.velocity[0])
        a += self.angle_k * (rng.random()-0.5)
        l: float = 1+self.velocity_k*(rng.random()-0.5)
        l = l if l < self.velocity_limit else self.velocity_limit
        self.velocity = l * np.array([np.cos(a), np.sin(a)])
        return None

    def update_position(self, dt: float) -> None:
        self.position += self.velocity * dt
        return None

    def boundary(self, xl: float, xr: float, yl: float, yr: float) -> None:
        x: float
        y: float
        x, y = self.position
        if x < xl or xr < x:
            self.velocity[0] *= -1
        if y < yl or yr < y:
            self.velocity[1] *= -1
        return None

    def add(self) -> None:
        self.lx.append(self.position[0])
        self.ly.append(self.position[1])
        return None


def hsv2rgb(h: float=0.0, s: float=1.0, v: float=1.0) -> str:
    rgb: np.ndarray = (255 * ((np.clip(np.abs(np.modf(h + np.array([0.0, 2.0, 1.0]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).round(0).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    rng: np.random.Generator = np.random.default_rng()
    offset: float = rng.random()
    saturation: float = 0.1
    value: float = 1.0
    bgc: str = hsv2rgb(offset, saturation, value)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    saturation = 0.5
    points: list[RandomWalk] = [
        RandomWalk(
            position=rng.random(2),
            velocity=rng.random()*np.array([np.cos(t), np.sin(t)])
        )
        for t in rng.random(11)
    ]
    for _ in range(50000):
        for p in points:
            p.update_velocity(rng=rng)
            p.update_position(dt=1e-3)
            p.boundary(xl=0, xr=1, yl=0, yr=1)
            p.add()
    hue: float = offset + 0.5
    for i, p in enumerate(points):
        saturation = 0.8 - 0.6*i/(len(points)-1)
        color: str = hsv2rgb(hue, saturation, value)
        ax.plot(p.lx, p.ly, linewidth=2, color=color)
        #ax.plot(p.position[0], p.position[1], linestyle="", marker="o", color=color)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], linewidth=1, color="black")
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
