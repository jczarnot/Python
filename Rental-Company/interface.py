from helperFunctions import format_text, read_number_ranged
from vehicle import Boat, Car
from loadFile import open_file, save_file
from findVehicle import FindVechicle
from datetime import date, datetime


class Interface:
    '''
    The main class of the program that communicates
    with the user and executes his requests
    '''
    def __init__(self, menu, vehicle_filename='vehicles.pickle',
                 reservation_filename="RentAndReservation.pickle"):
        self.menu = menu
        self._vehicle_filename = vehicle_filename
        self._reservation_filename = reservation_filename
        self._vehicles = []
        self.findVehicle = FindVechicle()
        self.RentAndReservation = None

    def main_loop(self):
        '''
        The main menu of the program.
        displays the functions that are available in the program
        Opens and saves function files
        database after each user query
        '''
        while True:
            print(self.menu)
            command = read_number_ranged("Enter your command: ", int, 1, 31)
            self.RentAndReservation = open_file(self._reservation_filename,
                                                self.RentAndReservation)
            self._vehicles = open_file(self._vehicle_filename, self._vehicles)
            self.RentAndReservation.cancel_missed_bookings()
            if command == 1:
                self.create_vehicle()
            elif command == 2:
                self.find_vehicle()
            elif command == 3:
                self.change_reservation()
            elif command == 4:
                self.cancel_reservation()
            elif command == 5:
                self.reservation_receiving()
            elif command == 6:
                self.rent_on_site()
            elif command == 7:
                self.rental_time_exceeded()
            save_file(self._vehicle_filename, self._vehicles)
            save_file(self._reservation_filename, self.RentAndReservation)
            if command == 8:
                exit()

    def choose_vehicle(self):
        '''
        Asks the user for the type of vehicle
        '''
        print("Press 0 to choose car or 1 to choose boat")
        vehicle_type = read_number_ranged("Enter number: ", int, 0, 1)
        return vehicle_type

    def create_vehicle(self):
        '''
        Creates a new vehicle with parameters specified by the user
        '''
        vehicle_type = self.choose_vehicle()
        brand = format_text('Enter brand: ')
        model = format_text('Enter model: ')
        engine = format_text('Enter type of engine: ')
        fuel_consumption = format_text('Enter fuel consumption per 100km: ')
        if vehicle_type == 0:
            passengers = format_text('Enter maximum number of passengers:')
            doors = format_text('Enter number of doors: ')
            new_car = Car(brand=brand, model=model, passengers=passengers,
                          doors=doors, engine=engine,
                          fuel_consumption=fuel_consumption)
            self._vehicles.append(new_car)
        if vehicle_type == 1:
            width = format_text('Enter width: ')
            length = format_text('Enter length: ')
            number_of_cabins = format_text('Enter number of cabins: ')
            boat = Boat(brand=brand, model=model, engine=engine,
                        fuel_consumption=fuel_consumption, length=length,
                        width=width, number_of_cabins=number_of_cabins)
            self._vehicles.append(boat)
        return self._vehicles

    def get_attributes_from_user(self, vehicle_type):
        '''
        Gets the names of attributes for the given vehicle type
        from the user and returns them as a list
        '''
        user_choice2 = []
        user_choice2.append(format_text('Enter brand or press 0 to skip '))
        user_choice2.append(format_text('Enter model or press 0 to skip '))
        user_choice2.append(
            format_text('Enter type of engine or press 0 to skip ')
        )
        user_choice2.append(
            format_text('Enter fuel consumption or press 0 to skip ')
        )
        if vehicle_type == 0:
            user_choice2.append(
                format_text('Enter number of passengers or press 0 to skip ')
            )
            user_choice2.append(
                format_text('Enter number of doors or press 0 to skip ')
            )
        elif vehicle_type == 1:
            user_choice2.append(format_text('Enter width or press 0 to skip '))
            user_choice2.append(
                format_text('Enter length or press 0 to skip ')
            )
            user_choice2.append(
                format_text('Enter number of cabins or press 0 to skip ')
            )
        return user_choice2

    def enter_rental_date(self):
        '''
        Asks the user for the vehicle rental date
        and checks its correctness
        '''
        incorrect_date = True
        while incorrect_date:
            try:
                rent_day = read_number_ranged(
                    "Enter rent day: ", int, 1, 31
                )
                rent_month = read_number_ranged(
                    "Enter rent month: ", int, 1, 12
                )
                rent_year = read_number_ranged(
                    "Enter rent year: ",
                    int,
                    date.today().year,
                    date.today().year + 1
                )
                self.rental_date = datetime(rent_year, rent_month, rent_day)
                incorrect_date = False
                return self.rental_date
            except ValueError:
                print("Please enter a valid date")

    def enter_return_date(self):
        '''
        Asks the user for the vehicle return date
        and checks its correctness
        '''
        incorrect_date = True
        while incorrect_date:
            try:
                return_day = read_number_ranged(
                    "Enter return day: ", int, 1, 31
                )
                return_month = read_number_ranged(
                    "Enter return month: ", int, 1, 12
                )

                return_year = read_number_ranged(
                    "Enter return year: ",
                    int,
                    date.today().year,
                    date.today().year + 1
                )
                self.return_date = datetime(return_year, return_month,
                                            return_day)
                incorrect_date = False
                return self.return_date
            except ValueError:
                print("Please enter a valid date")

    def split_vehicles(self):
        '''
        Separates vehicles according to their type
        '''
        cars = []
        boats = []
        for vehicle in self._vehicles:
            if vehicle.is_car:
                cars.append(vehicle)
            else:
                boats.append(vehicle)
        return cars, boats

    def search_by_availability_dates(self, cars, boats, vehicle_type,
                                     rental_date=None):
        '''
        Returns a list of vehicles that are
        available on the date specified by the user
        '''
        if rental_date is None:
            rental_date = self.enter_rental_date()
        return_date = self.enter_return_date()
        if vehicle_type == 0:
            cars = self.RentAndReservation.check_available_vehicles(
                cars, rental_date, return_date
            )
            if cars == []:
                print("Unfortunately we did not find any ")
                print("vehicle within this period")
                self.main_loop()
        if vehicle_type == 1:
            boats = self.RentAndReservation.check_available_vehicles(
                boats, rental_date, return_date
            )
            if boats == []:
                print("Unfortunately we did not find any ")
                print("vehicle within this period")
                self.main_loop()
        return cars, boats

    def refining_search(self, vehicle_type, boats, cars):
        '''
        Returns a list of vehicles with attributes specified by the user
        '''
        user_choice2 = self.get_attributes_from_user(vehicle_type)
        if vehicle_type == 0:
            for i in range(len(user_choice2)):
                if user_choice2[i] != '0':
                    new_car_lst = self.findVehicle.split_vehicle(
                        cars, i, vehicle_type, user_choice2[i]
                    )
                    if new_car_lst is not None:
                        cars = new_car_lst
                    else:
                        print("We did not find the specified vehicle")
                        print("in the database, make sure that the entered")
                        print("values ​​are correct and try again")
                        self.main_loop()
        if vehicle_type == 1:
            for i in range(len(user_choice2)):
                if user_choice2[i] != '0':

                    new_boats_lst = self.findVehicle.split_vehicle(
                        boats, i, vehicle_type, user_choice2[i]
                    )
                    if new_boats_lst is not None:
                        boats = new_boats_lst
                    else:
                        print("We did not find the specified vehicle")
                        print("in the database, make sure that the entered")
                        print("values ​​are correct and try again")
                        self.main_loop()
        return cars, boats

    def print_vehicles(self, vehicles):
        '''
        Writes out vehicles from the received list and asks
        the user to choose one of them
        '''
        if vehicles != [] and vehicles is not None:
            for i in range(len(vehicles)):
                print(i+1)
                print(vehicles[i])
            print("To choose vehicle enter the number above it, ")
            print("to exit press 0")
            vehicle_number = read_number_ranged("Enter number: ", int, 0,
                                                len(vehicles))
            if vehicle_number != 0:
                vehicle = vehicles[vehicle_number-1]
                return vehicle
            else:
                self.main_loop()
        else:
            print("We did not find a vehicle with the specified requirements")
            self.main_loop()

    def find_vehicle(self):
        '''
        Get information from the user about the type of search, details
        of this search and action on the selected vehicle
        '''
        cars, boats = self.split_vehicles()
        vehicle_type = self.choose_vehicle()
        print("Press 0 to search by availability dates,")
        print("1 to search by attributes or 2 to see all vehicles")
        searching_type = read_number_ranged("Enter number: ", int, 0, 2)
        if searching_type == 0:
            cars, boats = self.search_by_availability_dates(cars, boats,
                                                            vehicle_type)
        if searching_type == 1:
            cars, boats = self.refining_search(vehicle_type, boats, cars)
        if vehicle_type == 1:
            vehicle = self.print_vehicles(boats)
        else:
            vehicle = self.print_vehicles(cars)
        print("To reserve the selected vehicle, press 0, to edit press 1,")
        print("to delate press 2, to return to main menu press 3 ")
        user_choice3 = read_number_ranged("Enter number: ", int, 0, 3)
        if user_choice3 == 0:
            self.book_vehicle(searching_type, vehicle)
        if user_choice3 == 1:
            self.edit_vehicle(vehicle, vehicle_type)
        if user_choice3 == 2:
            self.remove_vehicle(vehicle)
        if user_choice3 == 3:
            self.main_loop()
        return vehicle, vehicle_type

    def remove_vehicle(self, vehicle):
        '''
        Removes the vehicle from the database
        and the associated booking
        '''
        ren_dat = vehicle.rental_dates()
        for key in ren_dat.keys():
            self.RentAndReservation.cancel_reservation(key)
        self._vehicles.remove(vehicle)
        return self._vehicles

    def edit_vehicle(self, vehicle, vehicle_type):
        '''
        Edits the selected vehicle based on the information
        received from the user
        '''
        print("Enter new attribute names or press 0 to leave them unchanged")
        user_choice2 = self.get_attributes_from_user(vehicle_type)
        for i in range(len(user_choice2)):
            if user_choice2[i] != '0':
                if i == 0:
                    vehicle.set_brand(user_choice2[i])
                if i == 1:
                    vehicle.set_model(user_choice2[i])
                if i == 2:
                    vehicle.set_engine(user_choice2[i])
                if i == 3:
                    vehicle.set_fuel_consumption(user_choice2[i])
                if vehicle_type == 0:
                    if i == 4:
                        vehicle.set_passengers(user_choice2[i])
                    if i == 5:
                        vehicle.set_doors(user_choice2[i])
                elif vehicle_type == 1:
                    if i == 4:
                        vehicle.set_width(user_choice2[i])
                    if i == 5:
                        vehicle.set_length(user_choice2[i])
                    if i == 6:
                        vehicle.set_number_of_cabins(user_choice2[i])
        return vehicle

    def book_vehicle(self, searching_type, vehicle):
        '''
        For the selected vehicle, checks its availability and,
        if possible, reserves it for the user
        '''
        if searching_type == 0:
            res_num = self.RentAndReservation.new_reservation(
                vehicle,
                self.rental_date,
                self.return_date
            )
            print(f"Your booking number is {res_num}")
            return res_num
        else:
            self.enter_rental_date()
            self.enter_return_date()
            result = self.RentAndReservation.check_vehicle_availability(
                vehicle,
                self.rental_date,
                self.return_date
            )
            if result:
                res_num = self.RentAndReservation.new_reservation(
                    vehicle,
                    self.rental_date,
                    self.return_date
                )
                print(f"Your booking number is{res_num}")
                return res_num
            else:
                print("Unfortunately, the selected vehicle is not")
                print("available on this date")
                self.main_loop()

    def change_reservation(self):
        '''
        asks the user for the reservation number and details of its
        modification, and changes it if possible
        '''
        print("Enter your reservation number")
        res_num = read_number_ranged("Enter number: ", int, 0, float('inf'))
        reservation = self.RentAndReservation.reservation()
        result = reservation.get(res_num)
        if result:
            choice1 = read_number_ranged("""To change the rental day prees 0 to
            leave unchanged press 1 : """, int, 0, 1)
            if choice1 == 0:
                rental_date = self.enter_rental_date()
            else:
                rental_date = None
            choice1 = read_number_ranged("""To change the return day prees 0 to
            leave unchanged press 1 : """, int, 0, 1)
            if choice1 == 0:
                return_date = self.enter_return_date()
            else:
                return_date = None

            result = self.RentAndReservation.change_reservation(res_num,
                                                                rental_date,
                                                                return_date)
            if result:
                print("Your booking has been changed")
                return True
            else:
                print("Unfortunately your booking could not be changed")
                return False
        else:
            print("We could not find the reservation within given number,")
            print("make sure you enter the correct details")
            return False

    def cancel_reservation(self):
        '''
        Deletes a reservation with the given number
        '''
        print("Enter your reservation number")
        res_num = read_number_ranged("Enter number: ", int, 0, float('inf'))
        result = self.RentAndReservation.cancel_reservation(res_num)
        if result:
            print("The reservation has been canceled")
            return True
        else:
            print("Unfortunately, the booking could not be canceled,")
            print("make sure you enter the correct details")
            return False

    def reservation_receiving(self):
        '''
        Asks the user for the reservation number
        and informs if the vehicle can be picked up
        '''
        print("Enter your reservation number")
        res_num = read_number_ranged("Enter number: ", int, 0, float('inf'))
        result = self.RentAndReservation.reservation_receiving(res_num)
        if result:
            print("The reservation has been received")
            return True
        else:
            print("The indicated reservation cannot be picked up,")
            print("make sure that the entered data is correct and try again")
            return False

    def rent_on_site(self):
        '''
        Displays a list of vehicles available for rental locally and rents
        the selected vehicle
        '''
        cars, boats = self.split_vehicles()
        vehicle_type = self.choose_vehicle()
        self.rental_date = self.RentAndReservation.today_date()
        cars, boats = self.search_by_availability_dates(cars, boats,
                                                        vehicle_type,
                                                        self.rental_date)
        if vehicle_type == 1:
            vehicle = self.print_vehicles(boats)
        if vehicle_type == 0:
            vehicle = self.print_vehicles(cars)
        res_num = self.book_vehicle(0, vehicle)
        return res_num

    def rental_time_exceeded(self):
        '''
        Displays vehicles that have exceeded their rental time
        '''
        vehicles_dict = self.RentAndReservation.rental_time_exceeded()
        if vehicles_dict != {}:
            for res_num, vehicles in vehicles_dict.items():
                print(f"Booking number {res_num} exceeded the rental time")
                print(f"Car number {vehicles.id()}")
                return vehicles_dict
        else:
            print("There are currently no vehicles that exceed the time limit")


menu = '''Tiny Vehicles

1. New vehicle
2. Find vehicle
3. Change reservation
4. Cancel reservation
5. Pick up your reservation
6. Rent on site
7. Check out-of-time rentals
8. Exit programm
 '''
interface = Interface(menu)
interface.main_loop()
