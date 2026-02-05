# 2) შექმენი კლასი Phone, რომელსაც ექნება:brand, storage(GB), price შექმენი 2 ტელეეფონი და დაბეჭდე რომელის არის უფრო ძვირი (if და property-ების გამოყენებით)

class Phone:
    def __init__(self, brand, storage, price):
        self.brand = brand
        self.storage = storage
        self.price = price

    def print_info(self):
        return(f'{self.brand} has {self.storage}GB of storage. The price is {self.price}$')


phone1 = Phone('Apple', 128, 1800)
phone2 = Phone('Samsung', 64, 1300)

if phone1.price > phone2.price:
    print(f'{phone1.brand} has a bigger price ')
else:
    print(f'{phone2.brand} has a bigger price ')

print()
print(phone1.print_info())
print(phone2.print_info())

