# Takes input of weather from the user
weather = input('What is the weather like?').lower()

# Evaluates whether input matches any of the following in order
if weather == 'rainy':
    print('You should bring an umbrella')
elif weather == 'sunny':
    print('You should bring a sunhat')
elif weather == 'snowy':
    print('Do you want to build a snowman')
elif weather == 'cloudy':
    print('I would bring a jacket it might be cold')
else:
    print("I've never heard of that weather before, sorry!")

