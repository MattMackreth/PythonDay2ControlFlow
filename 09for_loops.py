# For loops in python.
# used to iterate over collections - list and dictionaries

# x_crazy_landlords = ['Cruella de Ville', 'Donald Duck', 'Popeye']

# Syntax
# For <placeholder> in <list>:
    # Run block of code
# Placeholder is an internal variable with it's scope limited to a loop or function
# -----------------
# for landlord in x_crazy_landlords:
#     print(landlord)

# Exercise 1 - Print names with numbered formatting
# count = 0
# for landlord in x_crazy_landlords:
#     count += 1
#     print(str(count) + '. ' + landlord)

# Further loops

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [5, 6, 7]]

# for num in list_data:
#     print(num)

for data in embedded_list:
    print(data)
    for num in data:
        print(num * 2)


