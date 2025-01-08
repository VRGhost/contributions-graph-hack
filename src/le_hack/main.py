"""Main entrypoint"""

import typer

app = typer.Typer(pretty_exceptions_enable=False)


@app.command()
def serve(
    target_repo: str = typer.Argument(
        "git@github.com:VRGhost/_contributions_graph_hack_.git",
        help="The target repository",
    ),
):
    1 / 0


if __name__ == "__main__":
    app()
