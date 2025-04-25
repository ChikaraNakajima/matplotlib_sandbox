from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def cross_line_ellipse(a: float, b: float, c: float, d: float) -> list[float]:
    """
    x**2/a**2 + y**2/b**2 = 1
    y = d*(x-c)
    """
    if np.isinf(d):
        xp: float = c
        xm: float = c
        yp: float = b*np.sqrt(1-c*c/(a*a))
        ym: float = -yp
    else:
        p: float= 1/(a*a) + d*d/(b*b)
        q: float = -2*c*d*d/(b*b)
        r: float = c*c*d*d/(b*b)-1
        t: float = np.sqrt(q*q-4*p*r)
        xp: float = (-q+t)/(2*p)
        xm: float = (-q-t)/(2*p)
        yp: float = d*(xp-c)
        ym: float = d*(xm-c)
    return [xp, yp, xm, ym]


def main() -> None:
    # config
    fp: Path = Path(__file__).resolve().with_suffix(".png")
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.figsize"] = [19.2, 10.8]
    # 配色アイディア手帖 29
    colors: list[str] = [
        "#005eac",
        "#6f8aa9",
        "#003682",
        "#84c0da",
        "#d0deea",
        "#96b4ce",
        "#687543",
        "#514641",
        "#ad9d8f",
    ]
    # generate figure
    fig: plt.Figure
    ax: plt.Axes
    fig, ax = plt.subplots()
    # plot
    t: np.ndarray = np.linspace(0, 2*np.pi, 3601, endpoint=True)
    a: float = 16
    b: float = 9
    c: float = np.sqrt(a*a-b*b)
    n: int = 7
    ths: list[float] = [
        np.atan2(b*np.sin(0.5*np.pi+(i-n//2)*np.pi/12), a*np.cos(0.5*np.pi+(i-n//2)*np.pi/12)-c)
        for i in range(n)
    ]
    xp: float
    yp: float
    xm: float
    ym: float
    px: float
    py: float
    lw: float = 12
    for i, th in enumerate(ths):
        d = np.tan(th)
        xp, yp, xm, ym = cross_line_ellipse(a, b, c, d)
        if ym < yp:
            px = xp
            py = yp
        else:
            px = xm
            py = ym
        ax.plot([c, px, -c], [0, py, 0], color=colors[i], linewidth=lw)
        d = (py-0)/(px+c)
        xp, yp, xm, ym = cross_line_ellipse(a, b, -c, d)
        if ym > yp:
            px = xp
            py = yp
        else:
            px = xm
            py = ym
        ax.plot([-c, px, c], [0, py, 0], color=colors[i], linewidth=lw)
        d = (py-0)/(px-c)
    x: np.ndarray = a * np.cos(t)
    y: np.ndarray = b * np.sin(t)
    ax.plot(x, y, linewidth=lw, color=colors[-1])
    ax.plot([c, -c], [0, 0], linestyle="", color=colors[-1], marker="o", markersize=2*lw)
    # arrange
    #ax.set_xlim(-1.1, 1.1)
    #ax.set_ylim(-1.1, 1.1)
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_facecolor(colors[-2])
    fig.set_facecolor(colors[-2])
    fig.tight_layout()
    # output
    fig.savefig(fp)
    plt.cla()
    plt.clf()
    plt.close(fig)
    return None


if __name__ == "__main__":
    main()
