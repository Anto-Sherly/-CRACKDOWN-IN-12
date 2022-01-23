def get_game_word():
    word='hello'
    return word

def turns_left(turns):
    return turns-1

def initial_game():
    game=[]
    for j in range(len(get_game_word())):
        game.append('-')
    display_game(game)
    return game

def display_game(game):
    for i in game:
        print(i, end=" ")

def check_letter(game, letter):
    word=get_game_word()
    for i in range(len(word)):
        if game[i]=='-':
            if(word[i]==letter):
                game[i]=letter
                break

def check_win(game):
    win=True
    for i in game:
        if i=='-':
            return False
    return win

def play_game(game, turns):
    while(1):
        print("\nMake a guess")
        letter=input()
        check_letter(game, letter)
        display_game(game)
        if check_win(game):
            print("\nGame over you win")
            break
        turns=turns_left(turns)
        if(turns==0):
            print('\nNo guesses left. Game over!')
            break
        print('\nTurns left: '+str(turns))

def start_game():
    turns=len(get_game_word())+2
    game=initial_game()
    play_game(game,turns)

start_game()
