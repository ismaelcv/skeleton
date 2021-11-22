import pandas as pd
from matplotlib import pyplot as plt
from skeleton.plots.styles import STYLES


class base_scatter:

    """
    class that plots a base scatter plot.

    """

    def __init__(  # pylint: disable=too-many-arguments
        self, df: pd.DataFrame, x: str, y: str, labels: str = "", style: str = "base"
    ) -> None:
        self.df = df
        self.x = x
        self.y = y
        self.labels = labels
        self.style = STYLES[style]

        self._set_figsize()

    def _set_figsize(self, w: int = 12, h: int = 6) -> None:
        """
        Set figure size.

        """
        if w > 0 and h > 0:
            self.style["rcParams"]["figure.figsize"] = [w, h]

    def _set_styleParams(self, params: dict) -> None:
        """
        Set parameters for the plot.

        """
        for key, value in params.items():
            if key in self.style["styleParams"]:
                self.style["styleParams"][key] = value

    def show(self) -> None:

        if self.labels == "":
            colors = self.style["colors"]["1cat"]
        else:
            colors = (
                self.style["colors"]["2cat"]
                if len(self.df[self.labels].unique()) > 1
                else self.style["colors"]["1cat"]
            )

        plt.rcParams.update(self.style["rcParams"])
        plt.scatter(
            self.df[self.x], self.df[self.y], color=colors, s=self.style["styleParams"]["marker_size"]
        )

        if self.style["styleParams"]["marker_shadow"]:
            plt.scatter(
                self.df[self.x],
                self.df[self.y],
                color=colors,
                s=self.style["styleParams"]["marker_size"] * 4,
                alpha=0.2,
            )

        if "xticks" in self.style["styleParams"]:
            plt.xticks(**self.style["styleParams"]["xticks"])

        if "yticks" in self.style["styleParams"]:
            plt.yticks(**self.style["styleParams"]["yticks"])

        plt.ylabel(self.y)
        plt.xlabel(self.x)
