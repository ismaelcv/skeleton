import pandas as pd
from matplotlib import pyplot as plt
from skeleton.plots.styles import STYLES


class graph:

    """
    Generic class to genererate a plt graph
    """

    def __init__(self, df: pd.DataFrame, x: str, y: str, style: str = "base") -> None:
        self.df = df
        self.x = x
        self.y = y
        self.labels = ""
        self.styleParams = STYLES[style]["styleParams"]
        self.rcParams = STYLES[style]["rcParams"]
        self.colors = STYLES[style]["colors"]
        self._set_figsize()

        print(self.styleParams)

    def set_title(self, title: str) -> None:
        self.styleParams["title_style"]["text"] = title

    def set_subtitle(self, subtitle: str) -> None:
        self.styleParams["subtitle_style"]["text"] = subtitle
        self.styleParams["title_style"]["xy"] = (0.00, 1.13)

    def _set_figsize(self, w: int = 12, h: int = 6) -> None:
        if w > 0 and h > 0:
            self.rcParams["figure.figsize"] = [w, h]

    def _set_styleParams(self, params: dict) -> None:
        """
        Set parameters for the plot.

        """
        for key, value in params.items():
            if key in self.styleParams:
                self.styleParams[key] = value


class base_scatter(graph):
    def show(self) -> None:

        if self.labels == "":
            colors = self.colors["1cat"]
        else:
            colors = self.colors["2cat"] if len(self.df[self.labels].unique()) > 1 else self.colors["1cat"]

        plt.rcParams.update(self.rcParams)
        plt.scatter(self.df[self.x], self.df[self.y], color=colors, s=self.styleParams["marker_size"])

        if self.styleParams["marker_shadow"]:
            plt.scatter(
                self.df[self.x],
                self.df[self.y],
                color=colors,
                s=self.styleParams["marker_size"] * 4,
                alpha=0.2,
            )

        if "text" in self.styleParams["title_style"]:
            plt.annotate(**self.styleParams["title_style"])

        if "text" in self.styleParams["subtitle_style"]:
            plt.annotate(
                **self.styleParams["subtitle_style"],
            )

        if "xticks" in self.styleParams:
            plt.xticks(**self.styleParams["xticks"])

        if "yticks" in self.styleParams:
            plt.yticks(**self.styleParams["yticks"])

        plt.ylabel(self.y)
        plt.xlabel(self.x)
