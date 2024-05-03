""" This module provides BargoDrip CLI"""
# bargodrip/cli.py

from typing import Optional

import typer

from bargodrip import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool):
	if value:
		typer.echo(f"{__app_name__} v{__version__}")
		raise typer.Exit()

@app.callback()
def main(
	version: Optional[bool] = typer.Option(
		None,
		"--version",
		"-v",
		help="Display the application version and exit the program.",
		callback=_version_callback,
		is_eager=True,
	)
):
	return
