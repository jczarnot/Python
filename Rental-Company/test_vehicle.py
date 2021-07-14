from vehicle import Car, Boat
from loadFile import save_file
from datetime import datetime


def test_car_correct_attributes():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    assert car.brand() == "toyota"
    assert car.model() == "rv4"
    assert car.engine() == "disel"
    assert car.doors() == '5'
    assert car.fuel_consumption() == '5'
    assert car.passengers() == '5'


def test_car_set_brand():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_brand("audi")
    assert car.brand() == "audi"


def test_car_set_model():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_model("a4")
    assert car.model() == "a4"


def test_car_set_engine():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_engine("benzyna")
    assert car.engine() == "benzyna"


def test_car_set_fuell_consumption():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_fuel_consumption("10")
    assert car.fuel_consumption() == "10"


def test_car_set_passangers():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_passengers("6")
    assert car.passengers() == "6"


def test_car_set_doors():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    car.set_doors("3")
    assert car.doors() == "3"


def test_car_load_and_save_reservation_number():
    id_number = 1
    save_file("test_id_number.pickle", id_number)
    car = Car("toyota", "rv4", "disel", '5', '5', '5', "test_id_number.pickle")
    assert car.id() == id_number


def test_car_set_rental_dates():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    car.set_rental_dates(1, rental_date, return_date)
    assert car.rental_dates() == {1: (rental_date, return_date)}


def test_car_delate_rental_dates():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    reservation_number = 1
    car.set_rental_dates(reservation_number, rental_date, return_date)
    car.delete_reservation(reservation_number)
    assert car.rental_dates() == {}


def test_boat_correct_attributes():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    assert boat.brand() == "honda"
    assert boat.model() == "b40"
    assert boat.engine() == "disel"
    assert boat.width() == '500'
    assert boat.fuel_consumption() == '5'
    assert boat.length() == '200'
    assert boat.number_of_cabins() == '3'


def test_boat_set_brand():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_brand("audi")
    assert boat.brand() == "audi"


def test_boat_set_model():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_model("a4")
    assert boat.model() == "a4"


def test_boat_set_engine():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_engine("benzyna")
    assert boat.engine() == "benzyna"


def test_boat_set_fuell_consumption():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_fuel_consumption("10")
    assert boat.fuel_consumption() == "10"


def test_boat_set_width():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_width("600")
    assert boat.width() == "600"


def test_boat_set_length():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat.set_length("300")
    assert boat.length() == "300"


def test_boat_load_and_save_reservation_number():
    id_number = 1
    save_file("test_id_number.pickle", id_number)
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3',
                "test_id_number.pickle")
    assert boat.id() == id_number


def test_boat_set_rental_dates():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    boat.set_rental_dates(1, rental_date, return_date)
    assert boat.rental_dates() == {1: (rental_date, return_date)}


def test_boat_delate_rental_dates():
    boat = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    reservation_number = 1
    boat.set_rental_dates(reservation_number, rental_date, return_date)
    boat.delete_reservation(reservation_number)
    assert boat.rental_dates() == {}
