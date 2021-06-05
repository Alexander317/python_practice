class BankAccount:
    def __init__(self):
        self.name = 'Bill'
        self.account_id = 12345
        self.__balance = 20000
        self.__password = 'ABC'

    def change_balance(self, pswrd, new_balance_value):
        if self.__password == pswrd:
            self.__balance = new_balance_value
            print("Balance changed! New balance is", new_balance_value)
        else:
            print("Incorrect password!")


    def balance_info(self):
        print(f'{self.name} has {self.__balance}')


acc = BankAccount()
acc.balance_info()
acc.change_balance('АБВ', 10000)
acc.change_balance('ABC', 10000)
acc.balance_info()
