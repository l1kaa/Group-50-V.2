# 1) მოცემულია რიცხვების სია: nums = [1, 2, 3, 4, 5, 6]. იპოვე ყველა უნიკალური წყვილი (a, b), სადაც: a + b == 7
def unique_nums(nums,target):
    res = set()
    checked = set()
    for i in nums:
        sum = target - i
        if sum in checked:
            res.add((min(i, sum), max(i, sum)))
            checked.add(i)
        else:
            checked.add(i)
    return res

nums = [1, 2, 3, 4, 5, 6]

print(unique_nums(nums, 7))

# 2) მოცემულია სეტი და text ცვლადი: banned = {"bad", "ugly", "stupid"}, text = "This is a bad and ugly example". შეამოწმე: შეიცავს თუ არა ტექსტი აკრძალულ სიტყვებს, დაბეჭდე რომელი აკრძალული სიტყვაა ნაპოვნი

def check(set, txt):
    for i in set:
        if i in txt:
            return i

print(check({"bad", "ugly", "stupid"}, "This is a bad and ugly example"))

# 3) მოცემულია ორი სეტი: yesterday = {"Ana", "Nika", "Luka"}, today = {"Nika", "Saba", "Luka"}. იპოვე: ვინ დაემატა დღეს, ვინ დარჩა სიაში და ვინ ამოვარდა სიიდან

def check_updates(yesterday, today):
    new = today - yesterday
    stayed = yesterday & today
    removed = yesterday - today
    return f'\n Added Members: {new},\n Unchanged Members: {stayed},\n Removed Members: {removed}'

print(check_updates({"Ana", "Nika", "Luka"}, {"Nika", "Saba", "Luka"}))

# 4) მოცემულია სამი სეტი: required = {"python", "sql"}, forbidden = {"java"}, candidate = {"python", "java", "git"}. დაადგინე: აკმაყოფილებს თუ არა კანდიდატი მოთხოვნილებებს, რომელი წესები ირღვევა ან თუ ირღვევა საერთოდ.

def check_employee(required, forbidden, candidate):
    res = None
    for i in candidate:
        if i in required:
            res = True
        elif i in forbidden:
            res = False
    return res

required = {"python", "sql"}
forbidden = {"java"}
candidate = {"python", "java", "git"}

print(check_employee(required, forbidden, candidate))


# 5) მოცემულია სტრინგი "abccdefee" მოაშორე ის ასოები რომლებიც არის უნიკალური სტრინგში

def filter_func(str):
    res = ''
    for i in str:
        if i not in res:
            res += i
    return res

print(filter_func('abccdefee'))

# 6) დაწერე ფუნქცია is_unique(s), რომელიც აბრუნებს True-ს თუ სტრინგში ყველა სიმბოლო უნიკალურია.

def is_unique(s):
    return len(set(s)) == len(s)

print(is_unique('Heeeloo'))
print(is_unique('Helo'))


# 7) დაწერე ფუნქცია pair_sum(nums, target), რომელიც აბრუნებს ყველა უნიკალურ წყვილს (a, b) სადაც a + b == target. pair_sum([1,2,3,4,5,6], 7) დააბრუნე სეტში ტუპლების წყვილები რომლის დროსაც პირობა შესრულდება

def unique_nums(nums, target):
    res = set()
    checked = set()
    for i in nums:
        sum = target - i
        if sum in checked:
            res.add((min(i, sum), max(i, sum)))
            checked.add(i)
        else:
            checked.add(i)
    return res

nums = [1, 2, 3, 4, 5, 6]

print(unique_nums(nums, 7))