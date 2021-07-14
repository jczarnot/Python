def read_text(prompt):
    '''
    Displays a prompt and reads in a string of text.
    Keyboard interrupts (CTRL+C) are ignored
    returns a string containing the string input by the user
    '''
    while True:
        try:
            result = input(prompt)
            if result == '':
                print('Please enter text')
            else:
                break
        except KeyboardInterrupt:
            print('Please enter text')
    return result


def format_text(prompt):
    """
    Changes the letters of the string to
    lowercase and removes white space around it
    """
    result = read_text(prompt)
    result = result.lower()
    result = result.strip()
    return result


def read_number(prompt, function):
    '''
    Displays a prompt and reads in a floating point number.
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a float containing the value input by the user
    '''
    while True:
        try:
            number_text = read_text(prompt)
            result = function(number_text)
            break
        except ValueError:
            print('Please enter a number')
    return result


def read_number_ranged(prompt, function, min_value, max_value):
    '''
    Displays a prompt and reads in a number.
    min_value gives the inclusive minimum value
    max_value gives the inclusive maximum value
    Raises an exception if max and min are the wrong way round
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a number containing the value input by the user
    '''
    if min_value > max_value:
        raise Exception('Min value is greater than max value')
    while True:
        result = read_number(prompt, function)
        if result < min_value:
            print('That number is too low')
            print('Minimum value is:', min_value)
            continue
        if result > max_value:
            print('That number is too high')
            print('Maximum value is:', max_value)
            continue
        break
    return result
