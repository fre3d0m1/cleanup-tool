import click
from . import crud


@click.group()
def cli() -> None:
    print("Hello from cleanup-tool!")


cli.add_command(crud.analyze)
cli.add_command(crud.stats)
cli.add_command(crud.basic_organize)
