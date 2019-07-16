# While loops
# Syntax
# while <condition>
#   Block of code
#   *OPTIONAL* if <condition> break
import time
counter = 0

# Do block of code while condition is true
while counter <= 10:
    print(counter)
    counter += 1
    time.sleep(0.2)

print('part 2')
counter = 0

# Do block of code until condition is met
while True:
    print(counter)
    counter += 1
    time.sleep(0.2)
    if counter > 10:
        break  # Safeword to break out of a loop

print('fin')
