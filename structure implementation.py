1
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

print(months[2])

birthday_locations = ['home', 'vacation', 'hawaii', 'colorado', 'virginia']

birthday_locations.extend(['LA', 'San Fransisco', 'San Diego'])

print(birthday_locations)

i = 0

while i < len(birthday_locations):
    print(birthday_locations[i])
    i += 1
import random

sweepstakes_contestants = {
    # keys will be fname lname ticket#

    1: 'rich philip',
    2: 'regina wang',
    3: 'laura philip',
    4: 'richard philip',
    5: 'alison philip'
}

print(sweepstakes_contestants[random.randint(0, 4)])
