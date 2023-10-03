# Typer-based CLI entry point
import typer

# Create a Typer instance
app = typer.Typer()

# Define a sample command
@app.command()
def test(arg1: str, arg2: int):
    """
    My CLI command description.
    """
    typer.echo(f"Argument 1: {arg1}")
    typer.echo(f"Argument 2: {arg2}")

if __name__ == "__main__":
    app()
