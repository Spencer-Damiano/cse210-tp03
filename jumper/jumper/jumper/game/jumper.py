
class Jumper:
    """
    init 
    create jumper
    """

    def __init__(self):
        self.num_incorrect = 0

    def create_jumper(self):
        """
        if statements according to # of incorrect to decided what text output that we need
        """
        if self.num_incorrect == 0:
            jumper_0 = """
             ___  
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
            return jumper_0
        elif self.num_incorrect == 1:
            jumper_1 = """
            /___\ 
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
            return jumper_1
        elif self.num_incorrect == 2:
            jumper_2 = """
            \   / 
             \ /  
              0   
             /|\  
             / \  
            """
            return jumper_2
        elif self.num_incorrect == 3:
            jumper_3 = """
             \ /  
              0   
             /|\  
             / \  
            """
            return jumper_3
        elif self.num_incorrect == 4:
            jumper_4 = """
              X   
             /|\  
             / \  
            """
            return jumper_4
        
    def set_num_incorrect(self, increment):
        """
        set num_incorrect to increment
        """
        self.num_incorrect += increment
        return self.num_incorrect