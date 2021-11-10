
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
        letter_input = ""


    def start_game(self):
        self.do_inputs()
        self.do_updates()
        self.do_outputs()
        self.run_game()

    def do_inputs(self):
        letter_input = get_input
    def do_updates(self):
        verify_letter(letter_input)

    def do_outputs(self):
        print()

    def run_game(self):