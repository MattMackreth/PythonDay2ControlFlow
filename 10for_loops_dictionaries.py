# # For loop - using dictionaries / hashes
#
# # Syntax
# # for <placeholder> in <dict>:
#     # run block of code
# dict_data = {
#     'name': 'Bronson',
#     'money': 200,
# }
#
# for key in dict_data:
#     # When we iterate a hash dictionary the placeholder hold an individual key during each iteration
#     # We can use the key to access the values of our dictionary
#     print(key) + ' | ' + str(dict_data[key]))
#
# # Iterates over keys
#
#

embedded_dict_data = {
    1: {
        'name': 'Bronson',
        'money' : 200
    },
    2: {
        'name': 'Matt',
        'money': 100000
     },
    3: {
        'name': 'Alice',
        'money ': '1500'
    }
}
for item in embedded_dict_data.values():
    for field in item.values():
        print(field)
