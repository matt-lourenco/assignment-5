# Created by: Matthew Lourenco
# Created on: Oct 26 2016
# This is a program that lets you play a simplified version of 21 against the computer

import ui
from numpy import random

computer_cards = []
player_cards = []
computer_cards_shown = False

def setup_game():
    #sets up the game and undoes any changes previously made
    #input
    global computer_cards
    global player_cards
    global computer_cards_shown
    
    #these lines reset anything that may have changed since the last game
    computer_cards = []
    player_cards = []
    computer_cards_shown = False
    view['player_cards_label'].text = 'Your cards:'
    view['opponents_cards_label'].text = "Opponent's cards:     ?     ?     ?"
    view['reply_label'].text = ''
    
    #these lines randomize the computer's  3 cards
    for computer_card_index in range(0, 3):
        computer_cards.append(random.randint(1, 11))
    
    #randomize the player's  2 cards then show them
    for player_card_index in range(0, 2):
        player_cards.append(random.randint(1, 11))
        view['player_cards_label'].text = view['player_cards_label'].text + '     ' + str(player_cards[player_card_index])

def check():
    #reveals the computer's cards
    #process
    global computer_cards
    global computer_cards_shown
    
    view['opponents_cards_label'].text = 'Opponent' + "'" + 's cards:'
    
    for show_computer_card_index in computer_cards:
        view['opponents_cards_label'].text = view['opponents_cards_label'].text + '     ' + str(show_computer_card_index)
    
    computer_cards_shown = True

def find_winner():
    #finds the winner
    #process
    global computer_cards
    global player_cards
    
    #find each total
    computer_cards_total = 0
    player_cards_total = 0
    
    for computer_total_index in computer_cards:
        computer_cards_total = computer_cards_total + computer_total_index
        
    for player_total_index in player_cards:
        player_cards_total = player_cards_total + player_total_index
    
    #output
    #decide the winner by comparing the totals
    if player_cards_total == computer_cards_total:
        view['reply_label'].text = "Tie! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
    
    elif player_cards_total > 21 and computer_cards_total > 21:
        view['reply_label'].text = "Tie! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
    
    elif player_cards_total > computer_cards_total and player_cards_total < 22:
        view['reply_label'].text = "You Win! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
    
    elif computer_cards_total < 22:
        view['reply_label'].text = "You lose. \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
    
    else:
        view['reply_label'].text = "You Win! \n Opponent's total: " + str(computer_cards_total) + "\n Your total: " + str(player_cards_total)
    

def restart_touch_up_inside(sender):
    #when restart button is pressed this sets up the game and undoes any changes previously made
    setup_game()

def check_touch_up_inside(sender):
    #reveals computer's cards and prevents you from drawing. Then it finds the winner.
    global computer_cards_shown
    
    if computer_cards_shown == False:
        check()
        find_winner()

def draw_touch_up_inside(sender):
    #Adds a card to the player's hand, then reveals the computer's cards, then prevents you from drawing again, then finds the winner.
    #input
    global computer_cards_shown
    global player_cards
    
    if computer_cards_shown == False:
        
        #adds a card to the player's hand.
        player_cards.append(random.randint(1, 11))
        view['player_cards_label'].text = view['player_cards_label'].text + '     ' + str(player_cards[2])
        
        check()
        find_winner()

view = ui.load_view()
view.present('fullscreen')

setup_game()
#sets up the game when the game is launched
