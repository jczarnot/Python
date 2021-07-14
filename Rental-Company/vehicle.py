from loadFile import open_file, save_file


class Vehicle:
    '''
    Class that stores information about the
    attributes of vehicles and their rentals
    '''
    def __init__(self, brand, model, engine, fuel_consumption,
                 filename='idNumber.pickle'):
        self._id = None
        self.load_id_number(filename)
        self.save_id_number(filename)
        self._brand = brand
        self._model = model
        self._engine = engine
        self._fuel_consumption = fuel_consumption
        self._rental_dates = {}

    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_engine(self, engine):
        self._engine = engine

    def set_fuel_consumption(self, fuel_consumption):
        self._fuel_consumption = fuel_consumption

    def set_rental_dates(self, reservation_number, rental_date, return_date):
        self._rental_dates[reservation_number] = (rental_date, return_date)

    def delete_reservation(self, reservation_number):
        self._rental_dates.pop(reservation_number)

    def brand(self):
        return self._brand

    def model(self):
        return self._model

    def engine(self):
        return self._engine

    def fuel_consumption(self):
        return self._fuel_consumption

    def rental_dates(self):
        return self._rental_dates

    def id(self):
        return self._id

    def __str__(self):
        template = '''
        Brand: {0}
        Model: {1}
        Type of engine: {2}
        Fuel consumption per 100km: {3}
        '''

        return template.format(self._brand, self._model,
                               self._engine, self._fuel_consumption)

    def load_id_number(self, filename):
        '''
        Each vehicle has a unique number
        written and read from the file
        '''
        self._id = open_file(filename, self._id)
        return self._id

    def save_id_number(self, filename):
        save_file(filename, self._id+1)


class Car(Vehicle):
    '''
    The class that inherits from vehicle class.
    Contains additional attributes
    related to this type of vehicle
    '''
    def __init__(self, brand, model, engine, fuel_consumption, passengers,
                 doors, filename='idNumber.pickle'):
        super().__init__(brand, model, engine, fuel_consumption, filename)
        self._passengers = passengers
        self._doors = doors
        self.is_car = True

    def __str__(self):
        description = super().__str__()
        template = '''Max number of passengers: {0}
        Number of doors: {1}
        '''
        return description + template.format(self._passengers, self._doors)

    def set_passengers(self, passengers):
        self._passengers = passengers

    def set_doors(self, doors):
        self._doors = doors

    def doors(self):
        return self._doors

    def passengers(self):
        return self._passengers


class Boat(Vehicle):
    '''
    The class that inherits from vehicle class.
    Contains additional attributes
    related to this type of vehicle
    '''

    def __init__(self, brand, model, engine, fuel_consumption, width, length,
                 number_of_cabins, filename='idNumber.pickle'):
        super().__init__(brand, model, engine, fuel_consumption, filename)
        self._width = width
        self._length = length
        self._number_of_cabins = number_of_cabins
        self.is_car = False

    def set_width(self, width):
        self._width = width

    def set_length(self, length):
        self._length = length

    def set_number_of_cabins(self, number_of_cabins):
        self._number_of_cabins = number_of_cabins

    def width(self):
        return self._width

    def length(self):
        return self._length

    def number_of_cabins(self):
        return self._number_of_cabins

    def __str__(self):
        description = super().__str__()
        template = '''Total length: {0}
        Number of cabins: {1}
        Total width: {2}
        '''
        return description + template.format(self._length,
                                             self._number_of_cabins,
                                             self._width)
