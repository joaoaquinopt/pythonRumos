class BankAccount:
    def __init__(self, account_owner, money_available):
        self.__account_owner = account_owner
        self.__money_available = money_available

    def get_account_owner(self):
        return self.__account_owner

    def set_account_owner(self, new_account_owner):
        self.__account_owner = new_account_owner

    def get_money_available(self):
        return self.__money_available

    def withdraw(self, value):
        if value > self.__money_available:
            print("Você não tem saldo suficiente para levantar")
            return 0
        else:
            self.__money_available -= value
            return value

    def deposit(self, new_money_available):
        self.__money_available += new_money_available
        return self.__money_available


first_account = BankAccount("Miguel Oliveira", 5000)

print(f'BankAccount - Account Owner:{first_account.get_account_owner()[:6]}')
print(f'Money Available:{first_account.get_money_available()}')

print(f'Valor depositado: {first_account.deposit(10000)}')
print(f"Valor levantado: {first_account.withdraw(20000)}")
print(f'Saldo da conta: {first_account.get_money_available()}')
