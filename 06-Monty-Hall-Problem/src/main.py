import random


def monty_hall_game(switch_doors: bool) -> bool:
    """Simulate a single Monty Hall game

    :param switch_doors: True if want to switch the door
    :return: True if won the car, otherwise False
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    # doors which could be revealed (should not be initial_choice or car)
    doors_revealed = [i for i in range(3) if (i != initial_choice) and (doors[i] == 'goat')]
    
    # if the initial choice is car -> len(doors_revealed) = 2
    door_revealed  = random.choice(doors_revealed)

    if switch_doors:
        # change the choice
        final_choice = [i for i in range(3) if (i != initial_choice) and (i != door_revealed)][0]
    else:
        # do not change the choice
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_games(num_games: int = 1000) -> tuple:
    """Simulate Monty Hall game for 1000 (default) times

    :param num_games: number of playing game, defaults to 1000
    :return: number of wins in two considered situation
    """
    num_wins_without_switching = sum([monty_hall_game(switch_doors=False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(switch_doors=True) for _ in range(num_games)])

    return num_wins_without_switching, num_wins_with_switching


if __name__ == '__main__':
    number_of_games = 10000
    number_of_wins_without_switching, number_of_wins_with_switching = simulate_games(number_of_games)
    print(f'Winning rate without switching: {number_of_wins_without_switching/number_of_games * 100}%')
    print(f'Winning rate without switching: {number_of_wins_with_switching/number_of_games * 100}%')