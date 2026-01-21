#  1) შექმენით სია რომელშიც იქნება სახელები მოთავსებული შემდეგ კი დააბრუნეთ ისეთი სია რომელშიც მხოლოდ იქნება ის სახელები რომელიც იწყება "ა" ასოზე

names = ['Lika', 'Ana', 'Mariami', 'Anastasia', 'Sofio']

filtered_by_a = list(filter(lambda x: x.lower().startswith('a'), names))
print(filtered_by_a)