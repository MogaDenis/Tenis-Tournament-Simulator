import random


class PlayersService:
    def __init__(self, repo):
        self._repo = repo

    def add_player(self, new_player):
        self._repo.add_player(new_player)

    def remove_player(self, player):
        self._repo.remove_player(player)

    def get_all(self):
        return self._repo.get_all()

    def pick_random_player(self, list_of_players, picked_players):
        random_player = random.choice(list_of_players)

        while random_player in picked_players:
            random_player = random.choice(list_of_players)

        return random_player

    def pair_players(self, qualifying=False):
        """
            This function pairs the players. There are 2 cases: in qualifiers only the worst players are paired in order to eliminate enough players
        to make the final number of them a power of 2. In the other case, when the number is a power of 2, each player is randomly paired with another one. 

        :param qualifying: This flags if we need to play a qualifying type of round or not, defaults to False
        :return: List of tuples each of them containing 2 players that will play a match.
        """
        list_of_players = self.get_all()

        picked_players = []

        pairs = []

        if qualifying:
            length = len(list_of_players)
            number = length

            for i in range(length, -1, -1):
                while i % 2 == 0:
                    i //= 2

                if i == 1:
                    break
                else:
                    number -= 1

            # number is the largest power of 2 smaller of equal to the num of players. 

            list_of_players = list_of_players[length - (length - number) * 2:]

            for _ in range(len(list_of_players) // 2):
                player1 = self.pick_random_player(list_of_players, picked_players)

                picked_players.append(player1)

                player2 = self.pick_random_player(list_of_players, picked_players)

                picked_players.append(player2)

                pairs.append((player1, player2))

        else:
            for _ in range(len(list_of_players) // 2):
                player1 = self.pick_random_player(list_of_players, picked_players)

                picked_players.append(player1)

                player2 = self.pick_random_player(list_of_players, picked_players)
                
                picked_players.append(player2)

                pairs.append((player1, player2))

        return pairs