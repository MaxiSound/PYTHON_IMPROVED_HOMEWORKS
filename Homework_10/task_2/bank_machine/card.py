class Card:

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.balance_card = 0
        self.count_operations = 0

    def get_password(self):
        return self.__password
