from repository.players_repo import PlayersRepo
from services.players_service import PlayersService


class InvalidInputException(Exception):
    pass


class ConsoleUI:
    def __init__(self):
        self.repo = PlayersRepo()
        self.service = PlayersService(self.repo)

    def main_menu(self):
        print("\n\t\t~ Main menu ~")
        print("\n1 - Display all players.")
        print("2 - Play the tournament.")
        print("0 - Exit the application\n")

    def play_round(self, qualifying=False):
        pairs = self.service.pair_players(qualifying)

        for pair in pairs:
            winner = None
            print(f"\n{pair[0]} VS. {pair[1]}")

            user_choice = input("Choose the winner (1 or 2): ").strip()

            while user_choice not in ['1', '2']:
                self.invalid_input_message()
                user_choice = input("Choose the winner (1 or 2): ").strip()

            if user_choice == '1':
                winner = pair[0]
            else:
                winner = pair[1]

            for player in self.repo._list_of_players:
                if player == winner:
                    player.strength += 1

            loser = pair[0]
            if winner == loser:
                loser = pair[1]

            self.service.remove_player(loser)

    def print_players(self):
        list_of_players = self.service.get_all()

        for player in list_of_players:
            print(player)

    def read_user_choice(self):
        user_choice = input(">> ").strip()

        if user_choice not in ['0', '1', '2', '3']:
            raise InvalidInputException

        return user_choice

    def invalid_input_message(self):
        print("\nInvalid input!\n")

    def check_if_power_of_2(self, number):
        while number % 2 == 0:
            number //= 2

        return number == 1

    def start(self):
        while True:
            self.main_menu()

            while True:
                try:
                    user_choice = self.read_user_choice()
                    break
                except InvalidInputException:
                    self.invalid_input_message()

            if user_choice == '0':
                break

            elif user_choice == '1':
                # Display players. 
                self.print_players()

            elif user_choice == '2':
                # Play qualifying round.
                if not self.check_if_power_of_2(len(self.repo)):
                    # Play qualifying round. 
                    print("\n\t~ Qualifying round ~")
                    self.play_round(qualifying=True)

                while len(self.repo) > 2:
                    print(f"\n\t~ Last {len(self.repo)} ~")
                    self.play_round()

                # If we got here, it means it is the final. 
                print("\n\t~ Final ~")
                self.play_round()

                print(f"\nWINNER: {self.service.get_all()[0]}")


                
