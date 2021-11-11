from console import Console
from jumper import Jumper
from puzzle import Puzzle
class Director:
    """
    Methods
        init
        start game
        get inputs
        do outputs
        do updates
    """

    def __init__(self):
        self.console = Console()
        self.jumper = Jumper()
        self.puzzle = Puzzle()
        self.letter_input = ""


    def start_game(self):
        self.do_inputs()
        self.do_updates()
        self.do_outputs()
        self.run_game()

    def do_inputs(self):
        self.do_inputsletter_input = self.console.get_input()
    def do_updates(self):
        self.puzzle.verify_letter(self.letter_input)

    def do_outputs(self):
        print()

    def run_game(self):
        pass