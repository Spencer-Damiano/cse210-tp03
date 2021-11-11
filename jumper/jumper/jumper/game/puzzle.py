import random as rd
class Puzzle:

    def __init__(self):
        self.list_words = ["bear", "giraffe", "dog", "cat", "elephant", "computer"]
        self.masked_word = []
        self.current_word = ""
        self.length = 0
        self.errors = 0
        #self.masked_word.append(self.length * "_")

    def chose_word(self):
        """
        picks a word
        """
<<<<<<< Updated upstream
    
    def verify_letter(self):
=======
        self.current_word = rd.choice(self.list_words)
        self.length = len(self.current_word)
        return(self.current_word)


    def hided_word(self):
        """
        takes the word and makes the dashes
        """ 
        self.masked_word = ["_"] * self.length
        return(self.masked_word)

    def verify_leter(self, letter):
>>>>>>> Stashed changes
        """
        makes sure the letters are in the word
        """
        self.current_letter = letter
        if self.current_letter in self.current_word:
            self.masked_word = self.hided_word(letter)
        else:
            self.errors +=1


    def revel_letter(self):
        """
        shows letters
        """

        
def split_word(word):
    return [char for char in word]
word = "bear"
word_listed = split_word(word)
print(word)
letter = "r"
length = len(word)
masked = []
masked = ["_"] * length
#masked.append(length * "_")
print(masked[0])
print(masked[3])
#print(masked)
for x in range(length):
   if letter == word_listed[x]:
       masked[x] = letter
print(masked)