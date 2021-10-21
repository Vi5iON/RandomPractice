''' 
Table for game results.
-----------------------

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

'''

import random

"""
as per game rules user and computer select any one of these three.
"""
possibilities = {
    'rock': 'r',
    'paper': 'p',
    'scissor': 's'
}

# these are user winning senarios

win = {
    'rs': 'Rock smashes scissor. You win!!',
    'pr': 'Paper covers rock. You win!!',
    'sp': 'Scissor cuts paper. You win!!'
}

# these are computer winning senarios or user loosing senarios

loss = {
    'rp': 'Rock gets covered by paper. Computer wins!!',
    'ps': 'Paper is cut by scissor. Computer wins!!',
    'sr': 'Scissor is smashed by rock. Computer wins!!'
}

# if it doesn't fall in any of these senarios then they chose the same

#the main function of the program that starts the game
def game():
    print('!!!!!!!!!!!!!! Rock, Paper or Scissor !!!!!!!!!!!!!!\n')
    x_key = possibilities.get(user_turn(), 0)
    if x_key :
        y_key = possibilities.get(comp_turn())
        result(x_key+y_key)
    else :
        print('!! Invalid input !!')


#this function takes care of user choosing
def user_turn()->str:
    print('Your turn.\n-----------')
    user_input = read('Pick Rock, Paper or Scissor\n')
    print(f'\nYou have picked {user_input.lower()}.\n')
    return user_input.lower()


#this function takes care of computer choosing using random.choice()
#here we convert dict to list for random to navigate
def comp_turn()->str:
    print('Computer\'s turn.\n----------------')
    print('Computer is choosing between rock, paper and scissor.')
    comp_input = random.choice(list(possibilities))
    print(f'Computer has picked {comp_input.lower()}.\n')
    return comp_input.lower()


#based on user selection and computers selection this block decides the winner
def result(x:str):
    if win.get(x, 'none') != 'none' :
        print(win.get(x))
    elif loss.get(x, 'none') != 'none' :
        print(loss.get(x))
    else :
        print('Draw!! Both are the same.')


#this is used to read data from user
def read(msg: str)->str:
    return input(msg)


# keep the game running in a loop
if __name__ == '__main__' :
    print('!!Welcome!!')
    game()
    while True :
        want = read('\nWant to play more? (y/n)\n')
        if want == 'y' :
            game()
        else :
            break