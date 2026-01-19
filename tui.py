from textual.app import App, ComposeResult
from sorter import sorter
from textual.containers import Horizontal
from textual.widgets import Header , Footer , Input , Static , Button , Label

class FileSorter(App):
    CSS_PATH = "tui.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("s", "sort", "Sort"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Enter the directory path")
        yield Input(id="input")
        with Horizontal(classes="buttons"):
            yield Button("Sort", id="sort", variant='primary' )
            yield Button("Quit", id="quit", variant="error")

        yield Label('', id="static")

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.action_sort()

    async def action_quit(self) -> None:
        self.exit()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "sort":
            self.action_sort()
        # elif event.button.id == "quit":
        #     await self.action_quit()

    def action_sort(self) -> None:
        try:
            dir_path = self.query_one(Input).value
            if dir_path == "":
                self.query_one(Static).update("Please enter the directory path")
            sorter(dir_path)
            self.query_one(Static).update("the update is successful")
            self.query_one(Input).value = ""
            
        except Exception as e:
            self.query_one(Static).update(str(e))

if __name__ == "__main__":
    FileSorter().run()

