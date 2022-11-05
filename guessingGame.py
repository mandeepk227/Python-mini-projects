import random

def guess(x):

    low = 1
    high = x
    feedback = ''
    flag = True

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(
            f'Is {guess} too high (H) or too low (L) or correct (C) and to exit (B): ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'b':
            flag = False
            break
    if flag == True:
        print(f'Yay I found your Number , that is {guess}')
    elif flag == False:
        print('Hope to see you again')


guess(400)
