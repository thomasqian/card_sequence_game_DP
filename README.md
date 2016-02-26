# Card Sequence Game
##### Classic dynamic programming problem.

Description: A sequence of cards is produced, each with a different value.
The human player takes turn with the computer, each time selecting either the first or the last card in the sequence.
The goal of the game is to accumulate the greatest total value.

###### Constants
The following constants can be changed at the top of the file for different features.
```
  MAX_VALUE - specifies the greatest value that the cards will take on.
  LENGTH - specifies the number of cards that will be selected for the sequence. 
               Since values cannot repeat, LENGTH must be <= MAX_VALUE.
  predict - if true, the program will output the greatest value obtainable by the first player,
                assuming that both players play optimally, at the beginning of the game.
  pStart - if true, the player will be the first to pick. Otherwise, computer will have first move.
```
  
