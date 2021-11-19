from matplotlib import pyplot as plt
import pandas as pd


def base_scatter(df: pd.DataFrame, x: str, y: str, labels: str = "", style: dict = {}) -> None:
    """
    Creates a base scatter plot.

    """

    if labels == "":
        colors = style["colors"]["1cat"]
    else:
        colors = style["colors"]["2cat"] if len(df[labels].unique()) > 1 else style["colors"]["1cat"]

    plt.rcParams.update(style["rcParams"])
    # TODO: Add a way to modify figsize upstr
    plt.scatter(df[x], df[y], color=colors, s=50)
    plt.scatter(df[x], df[y], color=colors, s=200, alpha=0.2)

    if "xticks" in style["settings"]:
        plt.xticks(**style["settings"]["xticks"])

    if "yticks" in style["settings"]:
        plt.yticks(**style["settings"]["yticks"])

    plt.ylabel(y)
    plt.xlabel(x)
