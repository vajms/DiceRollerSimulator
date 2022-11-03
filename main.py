from random import randint

while True:
    command = input('Shall we roll the dice? (yes / y): ')
    if command == 'yes' or command == 'y':
        dice = {
            '1': '|         |\n|    O    |\n|         |',
            '2': '|         |\n|  O   O  |\n|         |',
            '3': '|         |\n|  O O O  |\n|         |',
            '4': '|  O   O  |\n|         |\n|  O   O  |',
            '5': '|  O   O  |\n|    O    |\n|  O   O  |',
            '6': '|  O O O  |\n|         |\n|  O O O  |',
        }
        print('\n|---------|')
        print(dice.get(str(randint(1, 6))))
        print('|---------|\n')
    else:
        break
print("Thank you for playing with!")
