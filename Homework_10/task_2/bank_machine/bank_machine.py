from card import Card


class Bank_machine:
    def __init__(self, card: Card):
        self.__balance_bank_machine = 100_000_000
        self.card = card

    @property
    def input_password(self):
        print("Введите пароль")
        password = int(input(""))
        if self.card.get_password() != password:
            print("Неверный пароль!")
            exit()

    # функция пополнения карты
    def add_many_in_card(self):
        print("Укажите сумму, на пополнение счёта")
        add_summa = int(input(""))
        if add_summa % 50 == 0:
            self.card.balance_card += add_summa
            self.__balance_bank_machine += add_summa
            print("Внесение денежных средств прошло успешно")
            self.card.count_operations += 1
            if self.card.count_operations % 3 == 0:
                self.card.balance_card += (add_summa / 100) * 3
                self.__balance_bank_machine -= (add_summa / 100) * 3
        else:
            print("Сумма внесения наличных должна быть кратна 50")

    # функция снятия наличных со счёта
    def remove_many(self):
        print("Укажите сумму которую вы хотели бы снять с вашего лицевого счёта")
        remove_summa = int(input(""))
        if remove_summa % 50 == 0:
            if remove_summa > self.card.balance_card:
                print("на вашем счёте недостаточно средств")
            elif remove_summa > self.card.balance_card:
                print(
                    "В банкоммате нет столько денежных средств \nпоробуйте воспользоваться другим банкоматом")
                self.card.balance_card -= remove_summa
                self.__balance_bank_machine -= remove_summa
            elif remove_summa > 5_000_000:
                self.card.balance_card -= (remove_summa +
                                           ((remove_summa / 100) * 10))
                self.__balance_bank_machine -= (remove_summa -
                                                ((remove_summa / 100) * 10))
                print("снятие денежных средств прошло успешно")
                print("был вычтен налог на богатство 10%")
                self.card.count_operations += 1
                if self.card.count_operations % 3 == 0:
                    self.card.balance_card += ((remove_summa / 100) * 3)
                    self.__balance_bank_machine -= ((remove_summa / 100) * 3)
            else:
                if (remove_summa / 100) * 1.5 > 30 and (remove_summa / 100) * 1.5 < 600:
                    self.card.balance_card -= (remove_summa +
                                               ((remove_summa / 100) * 1.5))
                    self.__balance_bank_machine -= (
                        remove_summa - ((remove_summa / 100) * 1.5))
                    print("комиссия за снятие наличных 1.5%")
                elif (remove_summa / 100) * 1.5 < 30:
                    self.card.balance_card -= (remove_summa + 30)
                    self.__balance_bank_machine -= (remove_summa - 30)
                    print("комиссия за снятие наличных = 30")
                elif (remove_summa / 100) * 1.5 > 600:
                    self.card.balance_card -= (remove_summa + 600)
                    self.__balance_bank_machine -= (remove_summa - 600)
                    print("комиссия за снятие наличных = 600")
                print("снятие денежных средств прошло успешно")
                self.card.count_operations += 1
        else:
            print("Сумма снятия наличных должна быть кратна 50")

    # функция запрос баланса
    def balance_user_card(self):
        return self.card.balance_card

    # функция запрос остатка денежных средств в банкомате
    def get_balance_bank_machine(self):
        return self.__balance_bank_machine

    # функция завершения сеанса
    def end_session(self):
        exit()
