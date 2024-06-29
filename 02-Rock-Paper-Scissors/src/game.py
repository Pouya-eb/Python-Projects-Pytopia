import random

class RockPaperScissors:
    """Main class for the game Rock, Paper, Scissors"""
    def __init__(self, name: str) -> None:
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name
    
    def get_user_choice(self) -> str:
        """Method to get the user's choice

        :return: User's choice
        """
        user_choice = input('Enter your choice (rock/paper/scissors): ').lower()
        if user_choice in self.choices:
            return user_choice
        else:
            print(f'Invalid choice, you must select from {self.choices}')
            return self.get_user_choice()

    def get_computer_choice(self) -> str:
        """Method to get computer's choice

        :return: Computer's choice
        """
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Method to decide game winner based on rules

        :param user_choice: The user's choice
        :param computer_choice: The computer choice 
        :return: game outcome
        """
        if user_choice == computer_choice:
            return 'It\'s a Tie'
        
        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        if (user_choice, computer_choice) in win_combinations:
            return 'Congratulations, you won!'
        
        return 'Oh no, the computer won!'
    
    def play(self):
        """Main method to run the game"""
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f'player choice: {user_choice}')
        print(f'computer choice: {computer_choice}')
        print(self.decide_winner(user_choice, computer_choice))

if __name__ == '__main__':

    game = RockPaperScissors('Pouya')
    while True: 
        game.play()
        continue_game = input('Do you want to play again? (Enter any key to continue or \'q\' to quit): ')
        if continue_game.lower() == 'q':
            break