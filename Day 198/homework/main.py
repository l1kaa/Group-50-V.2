# 1) მოცემულია სია nums = [1, 2, 3, 4, 5], map-ის და lambda-ს გამოყენებით მიიღე ახალი სია სადაც თითოეული რიცხვი გამრავლებულია 3-ზე

nums1 = [1, 2, 3, 4, 5]
multiplied_by_3 = list(map(lambda x: x * 3, nums1))
print(multiplied_by_3)

# 2) მოცემულია სია nums = [3, -1, 0, -7, 8, -2], filter-ის გამოყენებით დატოვე მხოლოდ უარყოფითი რიცხვები

nums = [3, -1, 0, -7, 8, -2]
negatives = list(filter(lambda x: x < 0, nums))
print(negatives)

# 3) მოცემულია სია nums = [1, 2, 3, 4, 5, 6], filter -> map ის გამოყენებით დატოვე ლუწი რიცხვები და თითოეული გაამრავლე 2-ზე

nums2 = [1, 2, 3, 4, 5, 6]
filtered = list(filter(lambda n: n % 2 == 0, nums2))
mapped = list(map(lambda i: i * 2, filtered))
print(mapped)

# 4) მოცემულია სია nums = [1, 2, 3, 4, 5, 6], filter -> map ის გამოყენებით აიყვანე ყველა რიცხვი კვადრატში და დატოვე მხოლოდ ის რიცხვები რომლებიც მეტია 20-ზე 

nums3 = [1, 2, 3, 4, 5, 6]
mapped2 = list(filter(lambda x: x > 20, map(lambda i: i ** 2, nums3)))
print(mapped2)

# 5) nums = [9, 2, 7, 4, 5, 6, 1], დატოვე მხოლოდ კენტი რიცხვები დაა დაალაგე ზრდადობით

nums4 = [9, 2, 7, 4, 5, 6, 1]
filtered_odds = list(filter(lambda y: y % 2 != 0, nums4))
filtered_odds.sort(key=lambda x: x)

print(filtered_odds)