from loadFile import open_file, save_file
from vehicle import Car, Boat
from reservation import RentAndReservation
from datetime import datetime
import pytest


def test_save_and_load_vehicles_file():
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("suzuki", "b45", "disel", '5', '500', '200', '3')
    boat3 = Boat("honda", "b45", "disel", '5', '500', '205', '3')
    boat4 = Boat("suzuki", "b45", "disel", '5', '500', '200', '4')
    boats = [boat1, boat2, boat3, boat4]
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '3', '6', '6')
    car3 = Car("toyota", "rv4", "disel", '3', '5', '5')
    car4 = Car("audi", "rv4", "disel", '5', '6', '6')
    cars = [car1, car2, car3, car4]
    vehicles = [cars, boats]
    filename = 'test_vehicles.pickle'
    save_file(filename, vehicles)
    new_vehicles = []
    new_vehicles = open_file(filename, new_vehicles)
    assert (new_vehicles[0][0]).brand() == (vehicles[0][0]).brand()
    assert (new_vehicles[1][0]).model() == (vehicles[1][0]).model()
    assert (new_vehicles[1][1]).engine() == (vehicles[1][1]).engine()
    assert (new_vehicles[0][1]).id() == (vehicles[0][1]).id()


def test_save_and_load_reservation_file():
    res = RentAndReservation()
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    res.new_reservation(car1, rental_date, return_date)
    filename = 'test_RentAndReservation.pickle'
    save_file(filename, res)
    n_reservation = None
    n_reservation = open_file(filename, n_reservation)
    assert res.reservation_number() == n_reservation.reservation_number()


def test_load_file_not_exist():
    with pytest.raises(SystemExit):
        new_vehicles = []
        filename = 'brak_pliku.pickle'
        new_vehicles = open_file(filename, new_vehicles)


def test_load_different_file():
    with pytest.raises(SystemExit):
        new_vehicles = []
        filename = 'plik_testowy.pickle'
        new_vehicles = open_file(filename, new_vehicles)


def test_load_changed_file():
    with pytest.raises(SystemExit):
        new_vehicles = []
        filename = 'changedFile.pickle'
        new_vehicles = open_file(filename, new_vehicles)
