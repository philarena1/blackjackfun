# blackjackfun
This Python program allows the simulation of different blackjack strategies, with different standard rules and custom numbers of players at the table

There are three main classes: Game, Person, and Hand. 

Each Game object has as many players as you want (7 is the max at a table, but who cares), along with the dealer. Each Person has different hands, consisting of the cards they are dealt, their actions (split, hit, double), and their bets.

To start a game:
``` python 
newGame = Game()
newGame.start_game()
newGame.get_fresh_deck()
```
This will create the objects needed to simulate a game, with the default settings
  - 2 players
  - 6 decks
  - 6x shuffling
