from game.console import Console
from game.jumper import Jumper
from game.puzzle import Puzzle
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
        self.run = True
        self.letter_input = ""
        self.jumper_guy = ""
        self.hidden_word = []

    def start_game(self):
        self.jumper_guy = self.jumper.create_jumper()
        self.puzzle.chose_word()
        self.hidden_word = self.puzzle.hided_word()
        self.run_game()

    def do_inputs(self):
        self.letter_input = self.console.get_input("Type in a letter: ")

    def do_updates(self):
        self.hidden_word = self.puzzle.verify_letter(self.letter_input)
        self.jumper_guy = self.jumper.create_jumper()

    def do_outputs(self):
        self.console.write(self.jumper_guy)
        self.console.write(self.hidden_word)

    def run_game(self):
        while self.run:
            self.do_inputs()
            self.do_updates()
            self.do_outputs()