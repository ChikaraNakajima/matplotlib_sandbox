import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["axes.grid"] = False
plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.figsize"] = [19.2, 10.8]
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 24
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["savefig.edgecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["xtick.bottom"] = False
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["ytick.minor.visible"] = False
plt.rcParams["ytick.left"] = False
plt.rcParams["ytick.right"] = False
plt.rcParams["xtick.labelbottom"] = False
plt.rcParams["ytick.labelleft"] = False


def ExpFormatter(digit=None):
    if isinstance(digit, int) and digit >= 1:
        pass
    else:
        digit = 1
    return ticker.StrMethodFormatter(r"$\mathrm{{{x:." + str(digit) + "e}}}$")
