from typing import Union

import pandas as pd
from matplotlib import pyplot as plt
from skeleton.plots.styles import STYLES


class graph:

    """
    Generic class to genererate a plt graph
    """

    def __init__(self, df: pd.DataFrame, x: str, y: str, style: str = "base") -> None:

        plt.rcParams.update(plt.rcParamsDefault)

        self.df = df
        self.x = x
        self.y = y
        self.styleParams = STYLES[style]["styleParams"]
        self.rcParams = STYLES[style]["rcParams"]
        self.colors = STYLES[style]["colors"]
        self._set_figsize()
        self.z = ""  # type: str
        self.main_categories = []  # type: list
        self.style = STYLES[style]

    def color_by(self, column_name: str) -> None:
        """
        Set the color for the plot.

        """

        if column_name not in self.df.columns:
            raise ValueError(f"{column_name} not in dataframe")

        self.z = column_name

        self.styleParams["color_by"] = column_name

    def focus_on(self, category: Union[str, list]) -> None:
        """
        Set the main category for the plot.

        """

        if isinstance(category, str):
            self.main_categories.append(category)
        elif isinstance(category, list):
            self.main_categories = category + self.main_categories

        print(self.main_categories)

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

        if self.z != "":
            categories = self.df[self.z].unique().tolist()

            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

        print(categories)
        plt.rcParams.update(self.rcParams)

        if len(categories) <= 1:
            color = self.colors["1cat"]
            plt.scatter(self.df[self.x], self.df[self.y], color=color, s=self.styleParams["marker_size"])

        else:
            colors = self.colors["ncats"]

            for i, category in enumerate(categories):

                color = colors[i % len(colors)]

                x_axis = self.df[self.x][self.df[self.z] == category]
                y_axis = self.df[self.y][self.df[self.z] == category]

                plt.scatter(x_axis, y_axis, color=color, s=self.styleParams["marker_size"])

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

        plt.show()

        print("hola")


class base_lineplot(graph):
    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        if self.z != "":
            categories = self.df[self.z].unique().tolist()
            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

        print(categories)
        plt.rcParams.update(self.rcParams)

        if len(categories) <= 1:
            color = self.colors["1cat"]
            plt.plot(self.df[self.x], self.df[self.y], color=color, **self.style["line_style"])

        else:
            colors = self.colors["ncats"]

            for i, category in enumerate(categories):

                color = colors[i % len(colors)]

                x_axis = self.df[self.x][self.df[self.z] == category]
                y_axis = self.df[self.y][self.df[self.z] == category]

                plt.plot(x_axis, y_axis, color=color, **self.style["line_style"])

        # plt.plot(self.df[self.x], self.df[self.y], color="#16264c", lw=1)

        # if "text" in self.styleParams["title_style"]:
        #     plt.annotate(**self.styleParams["title_style"])

        # if "text" in self.styleParams["subtitle_style"]:
        #     plt.annotate(
        #         **self.styleParams["subtitle_style"],
        #     )

        # if "xticks" in self.styleParams:
        #     plt.xticks(**self.styleParams["xticks"])

        # if "yticks" in self.styleParams:
        #     plt.yticks(**self.styleParams["yticks"])

        plt.ylabel(self.y)
        plt.xlabel(self.x)
