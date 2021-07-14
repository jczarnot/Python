import datetime
from loadFile import open_file, save_file


class RentAndReservation:
    def __init__(self, filename='reservation_number.pickle'):
        self._filename = filename
        self._reservation = {}
        self._rent = {}
        self._reservation_number = None
        self.load_reservation_number(self._filename)

    def reservation(self):
        return self._reservation

    def reservation_number(self):
        return self._reservation_number

    def filename(self):
        return self._filename

    def date_correctness(self, rental_date, return_date):
        '''
        Checks if the rental date is less than the return date
        '''
        today = self.today_date()
        if rental_date >= today and return_date > rental_date:
            return True
        else:
            return False

    def new_reservation(self, vehicle, rental_date, return_date):
        '''
        creates a new reservation with given number, dates,
        vehicle and add it to reservation dictionary in
        reservation class and vehicle class
        '''
        if self.date_correctness(rental_date, return_date):
            self._reservation[self._reservation_number] = vehicle
            vehicle.set_rental_dates(self._reservation_number, rental_date,
                                     return_date)
            self._reservation_number += 1
            self.save_reservation_number(self._filename)
            return self._reservation_number - 1

    def check_vehicle_availability(self, vehicle, rental_date, return_date):
        '''
        Checks if the given vehicle is available on given dates
        '''
        if self.date_correctness(rental_date, return_date):
            can_be_borrowed = True
            if len(vehicle.rental_dates()) > 0:
                for key, date in vehicle.rental_dates().items():
                    date_rental, date_return = date
                    if(
                        return_date == date_rental or
                        return_date == date_return or
                        rental_date == date_return or
                        rental_date == date_rental
                    ):
                        can_be_borrowed = False
                    elif (date_rental > rental_date and
                          date_rental < return_date):
                        can_be_borrowed = False
                    elif (date_return > rental_date and
                          date_return < return_date):
                        can_be_borrowed = False
                    elif(date_rental < rental_date and
                         date_rental < return_date and
                         date_return > rental_date and
                         date_return > return_date):
                        can_be_borrowed = False
            return can_be_borrowed
        else:
            print("Make sure the date entered is correct and try again")
            return False

    def check_available_vehicles(self, vehicle_lst, rental_date, return_date):
        '''
        Checks which vehicles from list are available in given dates
        '''
        if self.date_correctness(rental_date, return_date):
            available_vehicles = []
            for vehicle in vehicle_lst:
                if self.check_vehicle_availability(vehicle, rental_date,
                                                   return_date):
                    available_vehicles.append(vehicle)
            return available_vehicles

    def load_reservation_number(self, filename):
        '''
        Loads unique reservation number
        '''
        self._reservation_number = open_file(filename,
                                             self._reservation_number)
        return self._reservation_number

    def save_reservation_number(self, filename):
        '''
        Saves next reservation number
        '''
        save_file(filename, self._reservation_number)

    def cancel_reservation(self, reservation_number):
        '''
        Cancels reservation with given number
        '''
        vehicle = self._reservation.get(reservation_number)
        if vehicle:
            rental_dates = vehicle.rental_dates()
            d1, d2 = rental_dates.get(reservation_number)
            vehicle.delete_reservation(reservation_number)
            self._reservation.pop(reservation_number)
            return True
        else:
            return False

    def change_reservation(self, reservation_number, new_rental_date=None,
                           new_return_date=None):
        '''
        Checks if reservation can be change and changes it if can
        '''
        vehicle = self._reservation.get(reservation_number)
        if vehicle:
            rental_date = vehicle.rental_dates()
            d1, d2 = rental_date[reservation_number]
            self.cancel_reservation(reservation_number)
            if new_rental_date is None:
                new_rental_date = d1
            if new_return_date is None:
                new_return_date = d2
            if self.check_vehicle_availability(vehicle, new_rental_date,
                                               new_return_date):
                vehicle.set_rental_dates(reservation_number, new_rental_date,
                                         new_return_date)
                self._reservation[reservation_number] = vehicle
                return True
            else:
                vehicle.set_rental_dates(reservation_number, d1, d2)
                self._reservation[reservation_number] = vehicle
                return False
        else:
            print("Make sure you enter the correct booking number")
            print("and try again")
            return False

    def reservation_receiving(self, reservation_number):
        '''
        Transfers the booking to the rental dictionary
        where the currently rented vehicles are stored
        '''
        vehicle = self._reservation.get(reservation_number)
        if vehicle:
            self._rent[reservation_number] = vehicle
            self._reservation.pop(reservation_number)
            return True
        else:
            return False

    def cancel_missed_bookings(self):
        '''
        checks if in the reservation dictionary
        there are missed reservations that are out of time
        and if they are, deletes them.
        Returns a list of deleted reservation numbers
        '''
        cancel_bookings_number = []
        today = self.today_date()
        for reservation, vehicle in self._reservation.items():
            rental_dates = vehicle.rental_dates()
            rental_date, return_date = rental_dates.get(reservation)
            if today > rental_date:
                cancel_bookings_number.append(reservation)
        for reservation in cancel_bookings_number:
            self.cancel_reservation(reservation)
        return cancel_bookings_number

    def rental_time_exceeded(self):
        '''
        Lists rentals that have exceeded the return time
        '''
        time_exceeded = {}
        today = self.today_date()
        for reservation, vehicle in self._rent.items():
            rental_dates = vehicle.rental_dates()
            rental_date, return_date = rental_dates[reservation]
            if today > return_date:
                time_exceeded[reservation] = vehicle
        return time_exceeded

    def on_site_rental(self, vehicle, return_date):
        '''
        Checks whether the given vehicle can be rented on the spot
        '''
        today = self.today_date()
        if self.check_vehicle_availability(vehicle, today, return_date):
            reservation_number = self.new_reservation(vehicle, today,
                                                      return_date)
            self.reservation_receiving(reservation_number)
            return reservation_number

    def today_date(self):
        ''''
        Returns the current date
        '''
        today = datetime.date.today()
        year = today.year
        month = today.month
        day = today.day
        today = datetime.datetime(year, month, day)
        return today
