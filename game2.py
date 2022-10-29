'''Игра компьютер сам загадывает число и сам его угадывает'''

import numpy as np

def random_predict(number:int=1) -> int:
    """ guess number

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: attempts count
    """
    count = 0
    while True:
        count+=1
        predict_number=np.random.randint(0,101)
        if number == prediect_number:
            break
    return(count)

print(random_predict(10))