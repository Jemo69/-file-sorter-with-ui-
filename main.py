import sys 
from sorter import sorter
from streamlit.web import cli as stcli
from rich.console import Console
from tui import FileSorter
import typer

app = typer.Typer()
console = Console()
def run_streamlit():
    sys.argv = ["streamlit", "run", "gui.py"]
    sys.exit(stcli.main())



@app.command()
def gui():
    console.print("Running GUI")
    run_streamlit()
    
@app.command()
def sort(dir_path: str):
    console.print("Sorting files")
    sorter(dir_path)

@app.command()
def tui():
    console.print("Running TUI")
    file = FileSorter()
    file.run()

    
if __name__ == "__main__":
    app()
