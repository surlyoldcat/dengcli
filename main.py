import os

import click

from deng_context import DengConfig
import datashares.commands as dscommands
import openmetadata.commands as omcommands


@click.group()
@click.pass_context
def cli(ctx):
    cfg = DengConfig()
    cfg.set_context(ctx)


cli.add_command(dscommands.datashare)
cli.add_command(omcommands.openmetadata)
