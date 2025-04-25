from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class Boid:
    def __init__(
            self,
            position: np.ndarray,
            velocity: np.ndarray,
            mass: float,
        ) -> None:

        self.position: np.ndarray = position
        self.velocity: np.ndarray = velocity
        self.mass: float = mass

        self.initialize()

        self.lx: list[float] = [position[0]]
        self.ly: list[float] = [position[1]]
        return None

    def initialize(self) -> None:
        self.force: np.ndarray = np.zeros(2)
        self.force_s: np.ndarray = np.zeros(2)
        self.force_c: np.ndarray = np.zeros(2)
        self.alignment_v: np.ndarray = np.zeros(2)
        self.alignment_n: int = 0
        self.cohesion_p: np.ndarray = np.zeros(2)
        self.cohesion_n: int = 0
        return None

    def add(self) -> None:
        x: float
        y: float
        x, y = self.position
        self.lx.append(x)
        self.ly.append(y)
        return

    def boundary(self, xl: float, xr: float, yl: float, yr: float) -> None:
        x: float
        y: float
        x, y = self.position
        if x < xl or xr < x:
            self.velocity[0] *= -1
        if y < yl or yr < y:
            self.velocity[1] *= -1
        return None

    def limit_velocity(self, vl: float) -> None:
        l: float = np.linalg.norm(self.velocity)
        if vl < l:
            self.velocity *= vl/l
        return

    def update_force(self, ka: float, kc: float) -> None:
        self.force += self.force_s
        if self.alignment_n:
            self.force += self.alignment_v / self.alignment_n * ka
        if self.cohesion_n:
            self.force += self.cohesion_p / self.cohesion_n * kc
        return None

    def update_velocity(self, dt: float) -> None:
        self.velocity += self.force / self.mass * dt
        return None

    def update_position(self, dt: float) -> None:
        self.position += self.velocity * dt
        return None


def update_boids(
        boids: list[Boid],
        rs: float=0.1,
        ra: float=2.0,
        rc: float=2.0,
        ks: float=0.1,
        ka: float=0.5,
        kc: float=0.5,
        vl: float=1.0,
        dt: float=2e-5,
        xl: float=0.0,
        xr: float=1.0,
        yl: float=0.0,
        yr: float=1.0,
    ) -> list[Boid]:
    for i, b0 in enumerate(boids[:-1]):
        for b1 in boids[1+i:]:
            vp: np.ndarray = b0.position - b1.position
            l2: float = np.square(vp).sum()
            # separation
            if l2 < rs*rs:
                b0.force_s +=  vp * ks
                b1.force_s += -vp * ks
            # alignment
            if l2 < ra*ra:
                b0.alignment_n += 1
                b0.alignment_v += b1.velocity
                b1.alignment_n += 1
                b1.alignment_v += b0.velocity
            # cohesion
            if l2 < rc*rc:
                b0.cohesion_n += 1
                b0.cohesion_p += b1.position
                b1.cohesion_n += 1
                b1.cohesion_p += b0.position
    for b in boids:
        b.update_force(ka=ka, kc=kc)
        b.update_velocity(dt=dt)
        b.limit_velocity(vl=vl)
        b.update_position(dt=dt)
        b.boundary(xl=xl, xr=xr, yl=yl, yr=yr)
        b.add()
        b.initialize()
    return boids


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
    boids: list[Boid] = [
        Boid(
            position=rng.random(2),
            velocity=np.array([np.cos(2*np.pi*i), np.sin(2*np.pi*i)]),
            mass=1.0,
        )
        for i in rng.random(5)
    ]
    for i in range(100000):
        boids = update_boids(boids)
    for i, b in enumerate(boids):
        hue: float = offset + 0.5 + (i-0.5*len(boids)+0.5)/len(boids)*0.25
        color: str = hsv2rgb(hue, saturation, value)
        ax.plot(b.lx, b.ly, linewidth=6, color=color)
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], linewidth=2, color="black")
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
