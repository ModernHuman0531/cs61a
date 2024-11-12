import sqlite3
import readline
import random

points = {'A':1, 'J':11,'Q':12,'K':13}
points.update({n:n for n in range(2, 11)})

def hand_score(hand):
    total = sum([points[card] for card in hand])
    if total < 11 and 'A' in hand:
        total = total + 10
    return total

db = sqlite3.Connection("n.db")
sql = db.execute
# Put the pop out card in the cards database
sql("drop table if exists cards")
sql("create table cards(card, place);")

def play(card, place):
    sql("insert into cards values (?, ?)",(card, place))
    db.commit()

def score(who):
    # Take out the element in database.
    cards = sql("select * from cards where place = ?",[who])
    # Calculate the score of the card
    # Since hand_score's hand is a tuple, we should convert the cards to tuple.
    return hand_score([card for card, place in cards.fetchall()])

def bust(who):
    return score(who) > 21

player, dealer = 'player', 'dealer'
# deck should be the tuple
deck = list(points.keys()) * 4
random.shuffle(deck)

def play_hand(deck):
    play(deck.pop(), player)
    play(deck.pop(), dealer)
    play(deck.pop(), player)
    hidden = deck.pop()
    # The player decide whether hit or not, and check the score with bust
    while 'y' in input("Hit").lower():
        play(deck.pop(), player)
        if bust(player):
            print(player, "went bust")
            return 
        play(hidden, dealer)
    # If the dealer's score<17, then must hit.
    while score(dealer) < 17:
        play(deck.pop(), dealer)
        if bust(dealer):
            print(dealer, 'went bust')
            return 
    print(player, score(player)," and ",dealer, score(dealer))

# Until the card is less than 10, we keep playing this game.
while len(deck) > 10:
    print('\n dealing...')
    play_hand(deck)
    #Let already played card been discard
    sql("update cards set place = 'discard';")
