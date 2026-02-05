# 4) შექმენი კლასი BankAccount: რომელსაც ექნება owner, balance, currency. შექმენი 2 ანგარიში და დაბეჭდე: რომელი ანგარიშია უფრო დიდი თანხით.

class BankAccount:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

owner1 = BankAccount('Bill Gates', 1, 'USD')
owner2 = BankAccount('Lika Chkhikvadze', 99999999999999, 'USD')

print(f'{owner1.owner} has more money on his/her balance: {owner1.balance} {owner1.currency} than {owner2.owner} with balance: {owner2.balance} {owner2.currency}' if owner1.balance > owner2.balance else f'{owner2.owner} has more money on his/her balance: {owner2.balance} {owner2.currency} than {owner1.owner} with balance: {owner1.balance} {owner1.currency}')