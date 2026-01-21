# 1) მოცემულია სია numbers = [1, 2, 3, 4, 5, 12, 24, -1, -3, 44, 65, 43], lambdaს გამოყენებით დააბრუნე მხოლოდ ის რიცხვები რომლებიც მეტია 3-ზე.

numbers1 = [1, 2, 3, 4, 5, 12, 24, -1, -3, 44, 65, 43]
filtered1 = list(filter(lambda x: x > 3, numbers1))
print(filtered1)

# 2) მოცემუმლია სია numbers = [1, 2, 3, 4, 5, 6], lambdaს გამოყენებით ახალ სიაში ჩაამატე მხოლოდ ლუწი რიცხვები

numbers2 = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers2))
print(even)

# 3) მოცემულია words = ["hi", "hello", "world"], შექმენი lambda რომელიც აბრუნებს სტრინგების სიგრძეს

words = ["hi", "hello", "world"]
str_length = list(map(lambda s: len(s), words))
print(str_length)

# 4) მოცემულია სია numbers = [2, 3, 4, 5, 7], lambdaს გამოყენებით სიის ყველა წევრი გაამრავლე საკუთარ ინდექსებზე და შემდეგ ჩაამატე ეს რიცხვები ახალ ცარიელ ლისტში

numbers3 = [2, 3, 4, 5, 7]
multyply_by_index = list(map(lambda n: n * numbers3.index(n), numbers3))
print(multyply_by_index)

# 5) მოცემულია სია numbers = [12, 24, 55, 67, 98], შექმენი lambda, რომელიც აბრუნებს რიცხვის ციფრების ჯამს.

numbers4 = [12, 24, 55, 67, 98]
sum_of_digs = list(map(lambda d: sum(int(d) for d in str(d)), numbers4))
print(sum_of_digs)
