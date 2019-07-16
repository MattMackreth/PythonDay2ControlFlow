# list_names = ['Jojo', 'Matt', 'Tom', 'Fillipe', 'Bob', 'Mark']
# for name in list_names:
#     print('hello ' + name)

# list_scores = [1, 10, 3, 4, 5, 6]
# for score in list_scores:
#     print(str(score*10) + '%')

list_embedded_scores = [[10, 5, 2], [3, 4, 6]]
for score_list in list_embedded_scores:
    for score in score_list:
        print(score * 2)

