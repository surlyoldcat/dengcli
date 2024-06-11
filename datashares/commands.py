import click

from deng_context import DengConfig

# TODO extend context to include the 'datashare config' folder path


@click.group(invoke_without_command=True)
@click.pass_context
def datashare(ctx):
    if ctx.invoked_subcommand is None:
        # e.g. deng datashare
        click.echo('this should list all the datashare cfg files')


@click.command()
@click.pass_context
@click.argument('filename')
@click.option('--prompt/--no-prompt', default=False)
def create(ctx, filename, prompt):
    # e.g. deng datashare create [filename] --no-prompt
    # the 'prompt' bit is for asking confirmation for each step
    # in the process.
    click.echo(f"create a datashare from {filename}")
    cfg = DengConfig.from_context(ctx)
    cfg.prettyprint()
    # call a function in a Redshift module to do the actual work


@click.command()
@click.pass_context
@click.argument('filename')
@click.option('--prompt/--no-prompt', default=False)
@click.option('--cascade/--no-cascade', default=False)
def delete(ctx, filename, cascade, prompt):
    # e.g. deng datashare delete [filename] --cascade
    if click.confirm("Are you really really sure?"):
        # delete that thing
        click.echo("Deleting datashare!")

    if cascade and click.confirm("Shall I destroy your precious database?"):
        # delete all the other things
        click.echo("I AM DELETING ALL YOUR DATABASSES!")


datashare.add_command(create)
datashare.add_command(delete)
