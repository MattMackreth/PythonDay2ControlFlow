# Takes input of weather from the user
weather = input('What is the weather like? ').lower().strip()

# Evaluates whether input matches any of the following in order
if 'rainy' in weather and 'stormy' in weather:
    print('Bring a jacket and umbrella')
elif 'rainy' in weather or 'foggy' in weather:
    print('Bring an umbrella')
elif 'sunny' in weather:
    print('Wear a sunhat')
else:
    print('Live your best life')
