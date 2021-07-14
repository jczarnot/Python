import pickle


def load_file(filename, data):
    """
    Loads the data from the given filename
    Data are stored in binary as pickled file
    Exceptions will be raised if the load fails
    """
    with open(filename, 'rb') as input_file:
        data = pickle.load(input_file)
    return data


def open_file(filename, data):
    try:
        data = load_file(filename, data)
        return data
    except FileNotFoundError:
        print(f'We could not found {filename} file')
        print('make sure that file exist try again')
        exit()
    except OverflowError:
        print(f'We could not open {filename} file')
        print('make sure that file is correct and try again')
        exit()
    except pickle.UnpicklingError:
        print(f'We could not open {filename} file')
        print('make sure that file is pickle type and try again')
        exit()


def save_file(filename, data):
    """
    Saves the data to the given filename
    Data are stored in binary as pickled file
    Exceptions will be raised if the save fails
    """
    with open(filename, 'wb') as out_file:
        pickle.dump(data, out_file)
