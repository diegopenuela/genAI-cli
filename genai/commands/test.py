import typer

app = typer.Typer()

@app.command()
def test(arg1: str, arg2: int):
    """
    My CLI command description.
    """
    typer.echo(f"Argument 1: {arg1}")
    typer.echo(f"Argument 2: {arg2}")