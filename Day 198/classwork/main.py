# 1) map ფუნქციის და lambdaს გამოყენებით ლისტის ყველა ელემენტი აქციე uppercaseებად. names = ["nika", "ana", "aleqsandre', "daviti", "gabrieli", "luka"]

names = ["nika", "ana", "aleqsandre", "daviti", "gabrieli", "luka"]
convert_to_upper = list(map(lambda x: x.upper(), names))
print(convert_to_upper)

# 2) filter ფუნქციის და lambdaს გამოყენებით შექმენი ახალი სია და ახალ სიაში ჩაამატე მხოლოდ ის სიტყვები რომელთა სიგრძეც მეტია 4-ზე.  names = ["nika", "ana", "aleqsandre', "daviti", "gabrieli", "luka"]

names2 = ["nika", "ana", "aleqsandre", "daviti", "gabrieli", "luka"]
filter_by_length = list(filter(lambda s: len(s) > 4, names2))
print(filter_by_length)

# 3) sort ფუნქციის გამოყენებით დაალაგე (name, age) tuple-ების სია ასაკის მიხედვით. 

people = [
    ("Nika", 21),
    ("Ana", 19),
    ("Gio", 25)
]

people.sort(key=lambda x: x[1])
print(people)