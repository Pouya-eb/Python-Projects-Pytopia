import random


def validate_input(input_num: str) -> bool:
    """Validating the input based on rules and logic

    :param input_num: user guess
    :return: validation of input
    """
    if not input_num.isdigit():
        print('Invalid input. Please enter a number.')
        return False
    
    input_num = int(input_num)
    if input_num < 1 or input_num > 100:
        print('Invalid input. Please enter a number between 1 and 100.')
        return False
    
    return True


def start_game():
    """Main function for playing number guesser game"""
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        input_num = input('Enter your guess between 1 and 100: ')

        if input_num.lower() == 'q':
            print('Goodbye!')
            break

        if not validate_input(input_num):
            continue

        input_num = int(input_num)
        if input_num == rand_num:
            print(f'You guessed correctly! Your score is : {score}')
            play_again = input('Do you want to play again? (press y/Y or any key to quit.): ')
            if play_again.lower() == 'y':
                rand_num = random.randint(1, 100)
                score = 100
                continue
            else:
                print('Goodbye!')
                break

        elif input_num > rand_num:
            print('You guessed too high!')
        else:
            print('You guessed too low!')

        score -= 10
        score = max(score, 0)


if __name__ == '__main__':
    start_game()
