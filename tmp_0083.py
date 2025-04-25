from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class Planet:
    def __init__(self, mass: float, position: np.ndarray, velocity: np.ndarray, force: np.ndarray) -> None:
        self.mass: float = mass
        self.position: np.ndarray = position
        self.velocity: np.ndarray = velocity
        self.force: np.ndarray = force


def calc_force(p0: Planet, p1: Planet, g: float=1) -> np.ndarray:
    v: np.ndarray = p1.position - p0.position
    return g * p0.mass * p1.mass / np.square(v).sum() * v / np.linalg.norm(v)


def move(p0: Planet, p1: Planet, p2: Planet, dt: float=1e-5, g: float=1) -> tuple[Planet, Planet, Planet]:
    f01: np.ndarray = calc_force(p0, p1, g)
    f12: np.ndarray = calc_force(p1, p2, g)
    f20: np.ndarray = calc_force(p2, p0, g)
    p0.force =  f01 - f20
    p1.force = -f01 + f12
    p2.force =  f20 - f12
    p0.velocity += p0.force / p0.mass * dt
    p1.velocity += p1.force / p1.mass * dt
    p2.velocity += p2.force / p2.mass * dt
    p0.position += p0.velocity * dt
    p1.position += p1.velocity * dt
    p2.position += p2.velocity * dt
    return p0, p1, p2


def hsv2rgb(h: float, s: float, v: float) -> str:
    rgb: np.ndarray = np.round(255 * ((np.clip(np.abs(np.modf(h + np.array([0, 2, 1]) / 3)[0] * 6 - 3) - 1, 0, 1) - 1) * s + 1) * v).astype(int)
    return "#" + "".join(f"{i:02x}" for i in rgb)


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    bgc: str = hsv2rgb(0, 0.5, 1)
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    dt: float = 5e-6
    g: float = 1
    p3: Planet = Planet(3, np.array([ 1.0,  3.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]))
    p4: Planet = Planet(4, np.array([-2.0, -1.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]))
    p5: Planet = Planet(5, np.array([ 1.0, -1.0]), np.array([0.0, 0.0]), np.array([0.0, 0.0]))
    x3: list[float] = [p3.position[0]]
    y3: list[float] = [p3.position[1]]
    x4: list[float] = [p4.position[0]]
    y4: list[float] = [p4.position[1]]
    x5: list[float] = [p5.position[0]]
    y5: list[float] = [p5.position[1]]
    for _ in range(3160000):
        p3, p4, p5 = move(p3, p4, p5, dt, g)
        x3.append(p3.position[0])
        y3.append(p3.position[1])
        x4.append(p4.position[0])
        y4.append(p4.position[1])
        x5.append(p5.position[0])
        y5.append(p5.position[1])
    ax.plot([x3[0], x4[0], x5[0], x3[0]], [y3[0], y4[0], y5[0], y3[0]], linewidth=6, color=hsv2rgb(0.8, 0.5, 1))
    ax.plot(x3, y3, linewidth=6, color=hsv2rgb(0.4, 0.5, 1))
    ax.plot(x4, y4, linewidth=6, color=hsv2rgb(0.6, 0.5, 1))
    ax.plot(x5, y5, linewidth=6, color=hsv2rgb(0.2, 0.5, 1))
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
