from poker import Card, Deck, Poker
from tkinter import * 
import time
import os


def main ():
    NumInHands = eval(input ('Enter number of hands to play: '))
    while (NumInHands < 2 or NumInHands > 10):
        NumInHands = eval( input ('Enter number of hands to play: ') )
    game = Poker(NumInHands)
    game.deck_builder()  

    print('\n')

    for i in range(NumInHands):
        card_hand=game.hands[i]
        print ("Hand "+ str(i+1) + ": " , end="")
        game.check_Royal(card_hand)

    highest_score=max(game.tlist)
    highest_index=game.tlist.index(highest_score)

    another_answer = input('\nWho do you think will win? ')

    if another_answer in '12345678910':
        print ('\nHand ' + str(highest_index+1) + ' wins')

        
    '''The codes from here deal with the gif for the game '''

    root = Tk()

    frameCount = 20
    frames = [PhotoImage(file='dance-moves.gif',format = 'gif -index %i' %(i)) for i in range(frameCount)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCount:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
    label = Label(root)
    label.pack()
    root.after(0, update, 0)

    root.mainloop()
      
main()

