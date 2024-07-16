class BankAccount:
    def __init__(self, account_owner, total_money):
        self.__account_owner = account_owner
        self.__total_money = total_money

    def get_account_owner(self):
        return self.__account_owner

    def set_account_owner(self, owner):
        self.__account_owner = owner

    @property
    def total_money(self):
        return self.__total_money

    @total_money.setter
    def total_money(self, amount):
        self.__total_money = amount

    def __str__(self):
        return f"Conta de {self.__account_owner} com fundos no valor de {self.__total_money}"

    def withdraw(self, value):
        if value <= self.__total_money:
            self.__total_money -= value
            print(f"Levantou {value}. Total em conta: {self.total_money}")
        else:
            print("Fundos insuficientes.")

    def deposit(self, value):
        self.total_money += value
        print(f"Depositou {value}. Total em conta: {self.total_money}")


account = BankAccount("John Doe", 1000)
print(account)

print(account.total_money)

account.set_account_owner("Aires")
print(account)


account.withdraw(500)
account.deposit(200)
print(account)