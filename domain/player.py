class Player:
    def __init__(self, id, name, strength):
        self._id = id
        self._name = name
        self._strength = strength

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, new_strength):
        self._strength = new_strength

    def get_strength(self):
        return self._strength

    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - Strength: {self.strength}"

    def __repr__(self):
        return self.__str__()