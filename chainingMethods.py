class User:
    bank_name="First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("Name:", self.name, ", Balance:", self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance-=amount
        other_user.account_balance+=amount
        return self

jojo=User('Jojo', 'jojo@jo.jo')
jojo.make_deposit(100).make_deposit(50).make_deposit(20).make_withdraw(45).display_user_balance()

rick=User('Rick', 'rick@roll.com')
rick.make_deposit(5000).make_deposit(2500).make_withdraw(6000).make_withdraw(1000).display_user_balance()

jim=User('Jim', 'jim@jimminy.ca')
jim.make_deposit(10000).make_withdraw(100).make_withdraw(1000).make_withdraw(20).display_user_balance()

jojo.transfer_money(jim, 75).display_user_balance()
jim.display_user_balance()