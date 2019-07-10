# -*- coding: UTF-8 -*-
import random
import codecs
import copy

cardJokers = ('♛', '♕')
cardMarks = ('♠', '♥', '♦', '♣')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')
deck = []
for c in cardJokers:
    deck.append(c)
for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)
'''
shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)
    deck.remove(pickedCard)
'''
shuffledDeck=copy.copy(deck)
random.shuffle(shuffledDeck)

f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in pickedCard:
    f.write(card)
    f.write('\t')
f.close

numOfPlayers=3
cardsOfPlayer=int(len(shuffledDeck)/numOfPlayers)

print('\n--debug:s%d players,every one has %dccards:'%(numOfPlayers),cardsOfPlayer))
player1Cards=[]
for i in range(cardsOfPlayer):
    pickedCard=random.choice(shuffledDeck)
    player1Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)
print('\n--debug:Player1''s%d cards is--%s:'%(len(player1Cards),player1Cards))
print('--debug:Remained %d cards in shuffled deck is %s:'%(len(shuffledDeck),shuffledDecks))
player2Cards=[]
for i in range(cardsOfPlayer):
    pickedCard=random.choice(shuffledDeck)
    player2Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)

player3Cards=[]
for i in range(cardsOfPlayer):
    pickedCard=random.choice(shuffledDeck)
    player2Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)
