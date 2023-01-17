from domain.player import Player


class PlayersRepo:
    def __init__(self):
        self._list_of_players = []
        self.read_file()

    def get_all(self):
        self._list_of_players.sort(reverse=True, key=Player.get_strength)
        return self._list_of_players

    def read_file(self):
        open_file = open("repository/players.txt", "r")

        file_content = open_file.readlines()

        for line in file_content:
            if line != '\n':
                player_data = line.split(',')

                new_player = Player(player_data[0], player_data[1], int(player_data[2]))

                self.add_player(new_player)

    def add_player(self, new_player):
        self._list_of_players.append(new_player)

    def remove_player(self, player):
        self._list_of_players.remove(player)

    def __len__(self):
        return len(self._list_of_players)
