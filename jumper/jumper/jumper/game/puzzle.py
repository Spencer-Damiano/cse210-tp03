import random as rd
from game.jumper import Jumper

class Puzzle:

    def __init__(self, jumper):
        self.list_words = ["bear", "giraffe", "dog", "cat", "elephant", "computer"]
        self.masked_word = []
        self.current_word = ""
        self.current_letter = ""
        self.word_listed = []
        self.length = 0
        self.errors = 0
        self.jumper = jumper

    def chose_word(self):
        """
        picks a word
        
        """
        self.current_word = rd.choice(self.list_words)
        self.length = len(self.current_word)
        self.word_listed = [char for char in self.current_word]
        return(self.current_word)


    def hided_word(self):
        """
        takes the word and makes the dashes
        """ 
        self.masked_word = ["_"] * self.length
        return(self.masked_word)

    def verify_letter(self, letter):
        """
        makes sure the letters are in the word
        """
        self.current_letter = letter
        if self.current_letter in self.current_word:
            self.masked_word = self._reveal_letter(self.current_letter)
            return self.masked_word
        else:
            self.errors += 1
            self.jumper.set_num_incorrect(self.errors)
            return self.masked_word        

    def _reveal_letter(self, letter):
        """
        shows letters
        """
        self.current_letter = letter
        for x in range(self.length):
            if self.current_letter == self.word_listed[x]:
                self.masked_word[x] = self.current_letter
        return(self.masked_word)