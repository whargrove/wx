import typer

app = typer.Typer()


@app.command()
def hello_world() -> None:
    typer.echo("Hello world!")


def main() -> None:
    app()
