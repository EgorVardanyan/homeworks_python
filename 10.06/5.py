def convert_to_int(string):
    try:
        return int(string)
    except:
        raise ValueError('false argument')