def sport(a):
    if a == 'yes' or 'no':
        return 1
    else:
        return 0


name = input('Pls enter your name? ')
weight_kg = float(input('pls enter yours weight? (Kg) '))
weight_lb = str(weight_kg * 2.20462262)
print('dear ' + name + ' you are ' + weight_lb + ' pound')
height = float(input('pls enter your height? (cm) '))
height1 = height - 100
if height1 < weight_kg:
    print('its better to loos weight')
    answer = ''
    while answer != 'yes' and answer != 'no':
        answer = input('Do you go to gym every day? (yes/no) ')
        if answer == "yes":
            print('well done, keep going')
        if answer == "no":
            print('its time to sport')
        if answer != 'yes' and answer != 'no':
            print("oops! answer is incorrect, run again")
else:
    print('you are fit!!!')
