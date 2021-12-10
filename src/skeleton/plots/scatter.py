from typing import Optional, Union

import pandas as pd
from matplotlib import pyplot as plt
from skeleton.plots.utils import load_styles

STYLES = load_styles()


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
        self.notes = []  # type: list
        self.style = STYLES[style]

    def color_by(self, column_name: str) -> None:
        """
        Set the color for the plot.

        """

        if column_name not in self.df.columns:
            raise ValueError(f"{column_name} not in dataframe")

        self.z = column_name

        self.styleParams["color_by"] = column_name

        if self.main_categories == []:
            self.main_categories = list(self.df[column_name].unique())

    def focus_on(self, category: Union[str, list]) -> None:
        """
        Set the main category for the plot.

        """

        if isinstance(category, str):
            self.main_categories.append(category)
        elif isinstance(category, list):
            self.main_categories = category + self.main_categories

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

    def add_plot_style(self) -> None:

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

    def add_note(
        self,
        text: str,
        x: float,
        y: Optional[float] = None,
        category: Optional[str] = None,
        **kwargs: dict,
    ) -> None:

        if text is None:
            raise ValueError("An input text is required")

        if x is not None and y is not None:
            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (x, y),
                        "xytext": (x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )
        if category is not None and category not in self.main_categories:
            raise ValueError(
                f"{category} not in main categories. Available categories f{self.main_categories}"
            )

        if category is not None and self.z == "":
            raise ValueError(
                """
                It is not possible to specify a category on a single colored plot.
                Use color_by() to be able to specify a category
                """
            )

        if y is None:

            if category is None and len(self.main_categories) > 1:
                raise ValueError(
                    f"""
                Error: Ambiguity where to place the note You need to specify a category.
                Available categories {self.main_categories}"
                """
                )

            if category is None and self.z == "":
                selection = self.df[self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            elif category is not None:
                selection = self.df[self.df[self.z] == category][self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            closest_x = selection.loc[index_closest_x]
            y = self.df[self.df[self.x] == closest_x][self.y].iat[0]

            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (closest_x, y),
                        "xytext": (closest_x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )


class base_scatter(graph):
    def show(self) -> None:

        if self.z != "":
            categories = self.df[self.z].unique().tolist()

            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

        plt.rcParams.update(self.rcParams)

        if len(categories) <= 1:

            color = self.colors["1cat"]
            plt.scatter(self.df[self.x], self.df[self.y], color=color, **self.style["scatter_style"])

        else:

            colors = self.colors["ncats"]

            for i, category in enumerate(categories):

                color = colors[i % len(colors)]

                x_axis = self.df[self.x][self.df[self.z] == category]
                y_axis = self.df[self.y][self.df[self.z] == category]

                plt.scatter(x_axis, y_axis, color=color, **self.style["scatter_style"])

        for note, kwargs in self.notes:

            plt.annotate(**note, **kwargs)

        self.add_plot_style()


class base_lineplot(graph):
    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        if self.z != "":
            categories = self.df[self.z].unique().tolist()
            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

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

        for note, kwargs in self.notes:

            plt.annotate(**note, **kwargs)

        self.add_plot_style()
