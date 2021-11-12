
class Jumper:
    """
    init 
    create jumper
    """

    def __init__(self):
        self.num_incorrect = 0

    def create_jumper(self):
        print(f"jumper incorrect: {self.num_incorrect}")
        """
        if statements according to # of incorrect to decided what text output that we need
        """
        if self.num_incorrect == 0:
            jumper = """
             ___  
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 1:
            jumper = """
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 2:
            jumper = """
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 3:
            jumper = """
             \ /  
              0   
             /|\  
             / \  
            """
        elif self.num_incorrect == 4:
            jumper = """
              X   
             /|\  
             / \  
            """
        return jumper

    def get_jumper(self):
        """
        return jumper
        """
        return self.create_jumper()
        
    def set_num_incorrect(self, incorrect):
        """
        set num_incorrect to incorrect
        """
        self.num_incorrect = incorrect
        return self.num_incorrect