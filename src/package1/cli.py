import logging

import click

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", is_flag=True)
def main(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level)


@main.command()
@click.argument("name")  # positional argument
@click.option("-lan", "--language", default="en")
def greet(name: str, language: str) -> None:
    """
    :param name:
    :return:
    """

    if language == "es":
        print(f"Hola  {name}")
    else:
        print(f"Hello  {name}")
