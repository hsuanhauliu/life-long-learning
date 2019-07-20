from random import randint

def play():
    ''' Play the guessing game '''
    # randomly put the prize behind one of the doors
    correct_door = randint(0, 2)

    # player chooses a door
    guess = randint(0, 2)

    # if the player guessed it right the first time, he/she will lose
    # by switching
    if correct_door == guess:
        return 0

    # if the player guessed it wrong however, he/she will definitely win by
    # switching, since the host can only reveal the last remaining door.
    return 1

    
def simulation(num_of_runs):
    ''' Start our simulation '''
    counter = 0 # count how many wins

    for i in range(num_of_runs):
        counter += play()

    win_rate = float(counter) / num_of_runs
    print(f'Running {num_of_runs} simulations...')
    print("Average winning rate by switching:", win_rate)


def main():
    ''' Main '''
    num_of_runs = int(input('Number of runs? '))
    simulation(num_of_runs)


if __name__ == '__main__':
    main()
