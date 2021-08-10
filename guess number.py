import random

def run_guess(answer, guess):

    if 0<guess<11:
        answer == guess
        print('your are brilliant')
        return True
    else:
        print('hey bozo enter a number bw 1 and 10')
        return False

answer=random.randint(1,10)
while True:
    try:
        guess = int(input('enter a number bw 1 to 10'))
        if(run_guess(answer,guess)):
            break
    except ValueError as err:
        print('enter number')
        continue
