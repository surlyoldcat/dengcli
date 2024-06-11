import click

from deng_context import DengConfig


@click.group()
@click.pass_context
def openmetadata(ctx):
    pass


@click.command()
@click.pass_context
def publish(ctx):
    click.echo("No OpenMetadata for you!")
    cfg = DengConfig.from_context(ctx)
    cfg.prettyprint()


openmetadata.add_command(publish)
