def int_str(n):
    '''
        Print text format of the given integer.
        Example: int_str(448) -> four hundred forty-eight

        n (int): the number to be formatted.
    '''
    if not n:
        print()
        return

    units = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    tens_1 = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }

    tens = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }

    text = str(n)
    
    if len(text) == 1:
        print(units[text])
    elif len(text) == 2:
        if text.startswith('1'):
            print(tens_1[text])
        else:
            print(f'{tens[text[0]]}-{units[text[1]]}')
    elif len(text) == 3:
        print(f'{units[text[0]]} hundred', end=' ')
        int_str(int(text[1:]))
    elif len(text) == 4:
        print('one thousand', end=' ')
        int_str(int(text[1:]))



int_str(15)
int_str(26)
int_str(300)
int_str(401)