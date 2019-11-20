# Jupyter-GameOfNim
Source code for a interactive Game of Nim game developed in python 3.7 in Jupyter notebook. 
The Game of Nim is a mathematical game that features two players in turn removing sticks from a pile until all sticks have been removed. The game can be played in two different ways, either normally in which the player to pick up the last stick wins or misere style as the player to pick the last stick loses. In the game there are multiple rows of sticks in which the player can pick up one or more sticks pertaining to a single row, players.

The Game of Nim has been recognised as a mathematical game because it can be solved for any number of piles and sticks. This is done by calculating a Nim-Sum which is the cumulative ‘exclusive or’ (xor, ⊕) value from the amount of sticks in each pile. If we had three piles of x, y, z then the Nim-Sum would be calculated by x ⊕ y ⊕ z. We can use this Nim-Sum value to determine the optimal moves towards winning the game which will form the basis of our group’s solution.

In a normal game the players strategy is to end their turn in which the Nim-Sum is equal to zero, this also translates to the misere style in which the optimal strategy is also for the player to end their turn in which the Nim-Sum is zero. Although the Nim-Sum can be used to find optimal moves in the Game of Nim there are cases in which a player cannot win when their opponent utilises this strategy. When the Nim-Sum is initially equal to zero the player that goes first cannot make a move that results in a zero Nim-Sum which gives an advantage to the opponent, in the case where both players are performing optimal turns then the player who goes first will always lose.

Using this knowledge of the mathematical strategies for the Game of Nim we will be implementing the Nim-Sum strategy into a custom algorithm in which will choose optimal moves against a player.

This program will apply a misere style of the Game of Nim but could be translated to a normal style since the program’s strategy is the same. As we have stated since part of the strategy depends on whether a player goes first and the Nim-Sum value we will incorporate a feature for the player to either take the first move or opt for the program to take the first turn, thus giving the player a fair chance of winning. In this solution we need to encapsulate the following logic:

· Player can choose to initially go first or second

· The program performs optimal moves according to Nim-Sum calculations

· Program accepts input moves from a player

· Determine which player has won the misere game once all sticks are gone

I believe that this implementation of the Game of Nim will give the player the tools to win against a program that makes optimal moves and will successfully show many varying cases of sticks and piles.
