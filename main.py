def forest_room():
    print('\nThere is a bear in the forest.')
    print('Behind the bear is a cave.')
    print('The bear is eating yummy honey.')
    print('What would you like to do? (1 or 2)')
    print('1). Take the honey.')
    print('2). Taunt the bear.')

    answer = input('>')

    if answer == '1':
        game_over('The bear ate you!')
    elif answer == '2':
        print('\nYou tricked the bear. You can now enter the cave...')
        cave_room()
    else:
        game_over('You need to type a number')


def cliff_room():
    print('You jump off the cliff')
    print('Luckily, it was not that far of a jump.')
    print('There is an old man.')
    print('What would you like to do? (1 or 2)')
    print('1). Punch the old man.')
    print('2.) Talk to the old man.')

    answer = input('>')

    if answer == '1':
        game_over('You killed the old man! Look through his stuff for anything useful...')
    elif answer == '2':
        print('\nThe old man told you about a cave with a diamond in it. In the forest... You decide to climb the '
              'mountain again')
    else:
        game_over('You need to type a number')


def cave_room():
    print('You enter the cave. It is pitch black and you cannot see anything.')
    print('There is a blue shine! It must be the diamond!')
    print('You found the diamond and won!')

    play_again()


def game_over(reason):
    print('\n' + reason)
    print('Game Over')
    play_again()


def play_again():
    print('\nDo you want to play again? ( y or n)')
    answer = input('').lower()
    if 'y' in answer:
        start()
    else:
        exit()


def start():
    print('You wake up on the edge of a cliff.')
    print('There is a forest behind you, you can either jump off the cliff or go to the forest.("forest" or "cliff")')

    answer = input('>').lower()

    if 'forest' in answer:
        forest_room()
    elif 'cliff' in answer:
        cliff_room()
    else:
        game_over('Type either forest or cliff...')


start()
