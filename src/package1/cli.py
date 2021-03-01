import click
import logging


logger = logging.getLogger(__name__)

@click.group()
@click.option("-v", "--verbose", is_flag=True)
def main(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level)


@main.command()
@click.argument("name")  # positional argument
@click.option('-lan', '--language', default='en')
def greet(name,language):
    """
    :param name:
    :return:
    """

    if language == 'es':
        print(f'Hola  {name}')
    else:
        print(f'Hello  {name}')


