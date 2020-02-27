from __future__ import print_function
word = 'earring'
updatedSpaces = [('_ ') * len(word)]

def initialize():
    print (''.join(updatedSpaces))
    print('Lives = 6')
    getLetter()
def getLetter():
    global letter
    letter = raw_input('Your guess: ')
    check(letter)
    getLetter()
    
def check(letter):
    global lives
    global updatedSpaces
    global word
    if letter in word:
        for i in range(0,len(word)-1):
            earring=word.find(letter, i, len(word))
            if earring != -1:
                updatedSpaces[earring]=letter
    else:
        lives=lives-1
        print('Not in word,', lives, 'lives left!')
    print(updatedSpaces)
    getLetter()
def won ():
    if ('_') in updatedSpaces:
        getletter()
    else:
        print('You have guessed the word! Congradulations, you have won!')
        
def main():
    initialize()

main()



        
        
        