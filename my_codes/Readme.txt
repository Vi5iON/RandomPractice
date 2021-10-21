*******************Rock, paper or scissor*********************

These are three types of code written for 'rock, paper or scissor' game.

Classifying them into 2 types:
1. Rock_Paper_Sci_if
2. Rock_Paper_Sci and Rock_Paper_Sci_new

The major difference between two types is one is generic version which use if statments to compare win senarios (1)
and the other uses dictionaries to simplfy usage of if statments(2) to test win senarios.

(1) Rock_Paper_Sci_if
This code accepts a user input and randoms a computer input.
These inputs are nothing but choices of the players.
These inputs are then compared using multiple if statments to check different senarios and provide
results.

(2) Rock_Paper_Sci and Rock_Paper_Sci_new
This code uses the below table.
 
Table for game results.
-----------------------

(Rock_Paper_Sci)
 (y)computer |   rock(1)    paper(2)   scissor(3)
user(x)      |
--------------------------------------------------
rock(1)      |   1,1        1,2        1,3
             |              l          w
--------------------------------------------------
paper(2)     |   2,1        2,2        2,3
             |   w                     l
--------------------------------------------------
scissor(3)   |   3,1        3,2        3,3
             |   l          w
--------------------------------------------------

(Rock_Paper_Sci_new)
 (y)computer |   rock(r)    paper(p)   scissor(s)
user(x)      |
--------------------------------------------------
rock(r)      |   rr         rp         rs
             |              l          w
--------------------------------------------------
paper(p)     |   pr         pp         ps
             |   w                     l
--------------------------------------------------
scissor(s)   |   sr         sp         ss
             |   l          w
--------------------------------------------------

Wins and losses with repect to user.

There is no real difference between 'Rock_Paper_Sci' and 'Rock_Paper_Sci_new' except for keys in dictionarys.
Former uses tuples as keys and latter uses strings as keys.

Based on the above table we create 'win' and 'loss' dictionarys as shown in code, segregating it to find
user's win and loss senarios. Where keys are (x,y) or xy combination and values are results of the round.

This reduces comparing senarios to find win or loss case just by displaying values of dictionary based on keys
which are choice of user and computer.