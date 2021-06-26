name = input('Pls enter your name? ')
weight_kg = float(input('pls enter yours weight? (Kg) '))
weight_lb = str(weight_kg * 2.20462262)
print('dear ' + name + ' you are ' + weight_lb + ' pound')
height = float(input('pls enter your height? (cm) '))
height1 = height - 100
if height1 < weight_kg:
    print("*" * 20)
    print('its better to loos weight')
    print("*" * 20)
else:
    print("*" * 20)
    print('you are fit!!!')
    print("*" * 20)
sport = input('Do you go to gym every day? (yes/no) ')
if sport == "yes":
    print("*" * 20)
    print('well done, keep going')
    print("*" * 20)
elif sport == "no":
    print("*" * 20)
    print('its time to sport')
    print("*" * 20)
else:
    print("*" * 20)
    print("answer is incorrect, run again")
    print("*" * 20)
