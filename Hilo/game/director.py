from game.card import Card


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.
    Attributes:
        card(int): The value of the card drawn
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def _init_(self):
        """Constructor a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = ''
        self.card = 0
        self.card_text = ''
        self.guess_card = 0
        self.guess = ''
        self.points = 0
        self.new_points = 0
        self.stop_card = 0
        self.number_times = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        self.points = 300
        self.is_playing = True
        self.number_times = 0

        print(f'Hilo Game')
        print('')

        while self.is_playing:
            display_card = Card()
            self.card = display_card.choose()
            

            self.stop_card = self.card
            self.print_numbers()

            self.get_input()
            self.output()
            self.updates()

            if self.is_playing == False:
                break

            self.play_again()

    def print_numbers(self):
        """This function prints the selected card..
        Args:
            self (Director): an instance of Director.
        """
        print()
        print(f'The card is:')
    

        print(f'{self.card}')

    def get_input(self):
        """Ask the user to guess if the next card is higher or lower, and confirm the input is entered correctly (either "h" or "l" only).
        After the input is validated, call the function choose(self) and display a new card.
        Args:
            self (Director): an instance of Director.
        """

        while True:
            print()
            self.guess = input('Higher or Lower [h/l]: ').lower()

            if self.guess == 'l' or self.guess == 'h':

                while True:
                    display_card = Card()
                    self.guess_card = display_card.choose()
                    if self.guess_card == self.card:
                        continue
                    else:
                        break

                print(f'Next card was: {self.guess_card}')
                break

            else:
                print('Incorrect letter, try again.')
                continue

    def updates(self):
        """A method that determines the score for the entire game 
        and also makes sure to end game if points reach less than or equal to cero.
        Args:
            self (Director): an instance of Director.
        """

        self.points += self.new_points
        self.number_times += 1

        print(f'Your score is: {self.points}')

        if self.points <= 0:
            print('Game over!')
            self.is_playing = False


    def output(self):
        """A method that determines the score for one round of play
        Args:
            self (Director): an instance of Director.
        """

        if (self.card < self.guess_card and self.guess == 'l') or (self.card > self.guess_card and self.guess == 'h'):
            self.new_points = -75
        else:
            self.new_points = 100

    def play_again(self):
        """Ask the user if he wants to play another round.
        Args:
            self (Director): an instance of Director.
        """

        play = input('Play again [y/n]: ')

        if play == 'y':
            self.is_playing = True
        
        else:
            print('Game over!')
            self.is_playing = False