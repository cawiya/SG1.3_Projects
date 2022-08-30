"""defining a class"""
class BankAccount:

    """defining a class variable"""
    min_balance = 50000

    def __init__(self, first, last, accnumber, accbalance, cash_debit="", cash_credit=""):
        self.first_name = first
        self.last_name = last
        self.account_number = accnumber
        self.account_balance = accbalance
        self.cash_debit = cash_debit
        self.cash_credit = cash_credit

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

    def get_accnumber(self):
        return self.account_number

    def get_accbalance(self):
        return self.account_balance

    def set_deposit(self, cash_credit):

        self.cash_credit = cash_credit

        if cash_credit >= 0:
            self.account_balance = self.account_balance + self.cash_credit
            print(self.account_balance)

    def set_withdrawals(self, cash_debit):

        self.cash_debit = cash_debit

        if cash_debit < BankAccount.min_balance:
            self.account_balance = self.account_balance - self.cash_debit
            print(self.account_balance)

        else:
            print("You do not have sufficient funds")

# create an instance of the class
account1 = BankAccount("Tope", "Sebanjo", '0034567890', 100000)

# print attributes of the first instance
print(account1.get_first())
print(account1.get_last())
print(account1.get_accnumber())
print(account1.get_accbalance())

# deposit cash into the account
CASH_CREDIT = 50000
account1.set_deposit(CASH_CREDIT)

# attempt to withdraw cash from the account
CASH_DEBIT = 200000
account1.set_withdrawals(CASH_DEBIT)

CASH_CREDIT = 100000
account1.set_deposit(CASH_CREDIT)