from bank_machine import Bank_machine


class Menu:

    def __init__(self, bank_machine: Bank_machine):
        self.bank_machine = bank_machine
        bank_machine.input_password

    def menu_bank_card(self):
        print('''Здраствуйте, вы попали в личное меню для управления вашими денежными средствами!\n
✔Начальная сумма равна нулю
✔Допустимые действия: пополнить, снять, выйти
✔Сумма пополнения и снятия кратны 50 у.е.
✔Нельзя снять больше, чем на счёте
✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔При превышении суммы в 5 млн, вычитать налог на богатство 10%\n
веберите пункт для дальнейших действий''')
        while True:
            print('''1. Узнать баланс
2. Пополнить лицевой счёт
3. Снять наличные
4. Закончить сеанс
5. Для сотрудника инкасации''')
            point = input("")
            if point == "1":
                print(
                    f'Ваш баланс равен, {self.bank_machine.balance_user_card()}')
            elif point == "2":
                self.bank_machine.add_many_in_card()
            elif point == "3":
                self.bank_machine.remove_many()
            elif point == "4":
                print("Спасибо что воспользовались нашими услугами, всего доброго!")
                self.bank_machine.end_session()
            elif point == "5":
                print(
                    f'наличных в банкомате: {self.bank_machine.get_balance_bank_machine()}')
            else:
                print("вы выбрали не верный пункт, повторите попытку")
