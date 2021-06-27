sport = input('do you sport? yes/no ')
if sport == 'yes':
    print('well')
elif sport == 'no':
    print("go to gym ASAP!")
while answer(sport) == False:
    sport = input('do you sport? yes/no ')