# 2) შექმენი კლასი Product: რომელსაც ექნება name, price, quantity. შექმენი პროდუქტების სია და დაბეჭდე ყველაზე ძვირი და ყველაზე იაფი პროდუქტები

class Product:
    def __init__(self, name, price, quantity):
        self.name = name;
        self.price = price;
        self.quantity = quantity;

products = [
    Product("apple", 1, 300),
    Product("kiwi", 5, 70),
    Product("watermelon", 7, 150)
]

cheapest = min(products, key=lambda p: p.price)
most_expensive = max(products, key=lambda p: p.price)


print(f'The cheapest product is: {cheapest.name} with a price of ${cheapest.price}')
print(f'The most expensive product is: {most_expensive.name} with a price of ${most_expensive.price}')