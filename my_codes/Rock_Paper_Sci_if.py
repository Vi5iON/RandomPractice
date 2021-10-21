import random

#entry point of the application.
def main() :
    print('!!!!!!!!!!!!!! Rock, Paper or Scissor !!!!!!!!!!!!!!\n')
    user_choice = user_turn()
    computer_choice = comp_turn()
    result(user_choice, computer_choice)


#user's turn to pick
def user_turn()->str :
    return read('Choose between Rock, Paper or Scissor.\n')


#computer's turn to pick
def comp_turn()->str :
    print('Computer is choosing.')
    chose = random.choice(('rock', 'paper', 'scissor'))
    print(f'Computer chose {chose}.')
    return chose


#compute result using if statments
def result(user:str, comp:str) :
    if user.lower() == 'rock' and comp == 'paper':
        print('Rock covered by paper. Computer wins!!')
    elif user.lower() == 'rock' and comp == 'scissor':
        print('Rock smashes scissor. User wins!!')
    elif user.lower() == 'paper' and comp == 'rock':
        print('Paper covers rock. User wins!!')
    elif user.lower() == 'paper' and comp == 'scissor':
        print('Paper is cut by scissor. Computer wins!!')
    elif user.lower() == 'scissor' and comp == 'rock':
        print('Scissor is crushed by rock. Computer wins!!')
    elif user.lower() == 'scissor' and comp == 'paper':
        print('Scissor cuts paper. User wins!!')
    else :
        print('Both chose same. Draw!!!')

#to read input user
def read(msg: str)->str :
    return input(msg+'\n')

if __name__ == '__main__' :
    main()