from reservation import RentAndReservation
from vehicle import Car, Boat
from datetime import datetime
import pytest
from loadFile import save_file


def test_new_reservation():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    reservation_number = reservation.reservation_number()
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    reservation_number_after = reservation.reservation_number()
    finall_dict = {reservation_number: (rental_date, return_date)}
    assert car.rental_dates() == finall_dict
    assert reservation_number_after == reservation_number + 1


def test_load_and_save_reservation_number():
    reservation_number = 1
    save_file("test_reservation_number.pickle", reservation_number)
    reservation = RentAndReservation("test_reservation_number.pickle")
    assert reservation.reservation_number() == reservation_number


def test_reservation_filename():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    assert reservation.filename() == filename


def test_date_correctness():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 2)
    result = reservation.date_correctness(rental_date, return_date)
    assert result is True


def test_date_incorrect():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    rental_date = datetime(2021, 1, 28)  # rental date > return date
    return_date = datetime(2021, 1, 2)  # return date < today date
    result = reservation.date_correctness(rental_date, return_date)
    assert result is False


def test_date_correctness_incorrect_day():
    with pytest.raises(ValueError):
        datetime(2021, 2, 31)


def test_vehicle_can_be_borrowed1():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is True


def test_vehicle_can_be_borrowed2():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 3, 10)
    return_date = datetime(2021, 3, 20)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 9)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is True


def test_vehicle_can_be_borrowed3():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 3, 10)
    return_date = datetime(2021, 3, 20)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 3, 28)
    return_date = datetime(2021, 3, 30)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is True


def test_vehicle_can_not_be_borrowed1():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed2():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 1, 29)
    return_date = datetime(2021, 2, 1)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed3():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 1, 29)
    return_date = datetime(2021, 2, 10)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed4():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 2, 2)
    return_date = datetime(2021, 2, 10)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed5():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 2, 20)
    return_date = datetime(2021, 2, 26)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 2, 26)
    return_date = datetime(2021, 2, 28)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed6():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 2, 20)
    return_date = datetime(2021, 2, 26)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 2, 21)
    return_date = datetime(2021, 2, 25)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_vehicle_can_not_be_borrowed7():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    rental_date = datetime(2021, 2, 20)
    return_date = datetime(2021, 2, 26)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 2, 21)
    return_date = datetime(2021, 2, 28)
    result = reservation.check_vehicle_availability(car, rental_date,
                                                    return_date)
    assert result is False


def test_check_available_vehicles():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("suzuki", "b45", "disel", '5', '500', '200', '3')
    boat3 = Boat("honda", "b45", "disel", '5', '500', '205', '3')
    boat4 = Boat("suzuki", "b45", "disel", '5', '500', '200', '4')
    rental_date = datetime(2021, 3, 10)
    return_date = datetime(2021, 3, 20)
    reservation.new_reservation(boat1, rental_date, return_date)
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 9)
    reservation.new_reservation(boat2, rental_date, return_date)
    boats = [boat1, boat2, boat3, boat4]
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 9)
    vehicles = reservation.check_available_vehicles(boats, rental_date,
                                                    return_date)
    assert vehicles == [boat1, boat3, boat4]


def test_check_available_vehicles2():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("suzuki", "b45", "disel", '5', '500', '200', '3')
    boat3 = Boat("honda", "b45", "disel", '5', '500', '205', '3')
    boat4 = Boat("suzuki", "b45", "disel", '5', '500', '200', '4')
    rental_date = datetime(2021, 1, 29)
    return_date = datetime(2021, 3, 20)
    reservation.new_reservation(boat1, rental_date, return_date)
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 9)
    reservation.new_reservation(boat2, rental_date, return_date)
    boats = [boat1, boat2, boat3, boat4]
    rental_date = datetime(2021, 1, 28)
    return_date = datetime(2021, 2, 9)
    vehicles = reservation.check_available_vehicles(boats, rental_date,
                                                    return_date)
    assert vehicles == [boat3, boat4]


def test_cancel_reservation():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    rental_date = datetime(2021, 1, 29)
    return_date = datetime(2021, 3, 20)
    number = reservation.new_reservation(boat1, rental_date, return_date)
    assert reservation.cancel_reservation(number) is True
    assert boat1.rental_dates() == {}
    assert reservation.reservation() == {}


def test_cancel_reservation_incorrect_reservation_number():
    filename = 'reservation_number.pickle'
    reservation = RentAndReservation(filename)
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    rental_date = datetime(2021, 1, 29)
    return_date = datetime(2021, 3, 20)
    number = reservation.new_reservation(boat1, rental_date, return_date)
    assert reservation.cancel_reservation(number+1) is False


def test_change_rental_date_in_reservation():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    new_rental_date = datetime(2021, 1, 31)
    result = reservation.change_reservation(number, new_rental_date)
    assert result is True


def test_change_reservation_incorrect():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    reservation.new_reservation(car, rental_date, return_date)
    rental_date = datetime(2021, 2, 3)
    return_date = datetime(2021, 2, 6)
    number1 = reservation.new_reservation(car, rental_date, return_date)
    new_rental_date = datetime(2021, 1, 31)
    result = reservation.change_reservation(number1, new_rental_date)
    assert result is False


def test_change_return_date_in_reservation():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    new_return_date = datetime(2021, 1, 31)
    result = reservation.change_reservation(number,
                                            new_return_date=new_return_date)
    assert result is True
    assert car.rental_dates() == {number: (rental_date, new_return_date)}


def test_change_return_and_rental_date_in_reservation():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    new_rental_date = datetime(2021, 2, 1)
    new_return_date = datetime(2021, 2, 6)
    result = reservation.change_reservation(number, new_rental_date,
                                            new_return_date)
    assert result is True
    assert car.rental_dates() == {number: (new_rental_date, new_return_date)}


def test_reservation_receiving():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    result = reservation.reservation_receiving(number)
    assert result is True
    assert reservation._rent == {number: car}


def test_reservation_receiving_fail():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    result = reservation.reservation_receiving(number+1)
    assert result is False
    assert reservation._rent != {number: car}


def test_time_exceeded():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 5)
    return_date = datetime(2021, 1, 20)
    reservation_number = 0
    reservation._rent[reservation_number] = car
    car.set_rental_dates(reservation_number, rental_date, return_date)
    time_exceeded = reservation.rental_time_exceeded()
    assert time_exceeded == {reservation_number: car}


def test_on_site_rental():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    return_date = datetime(2021, 2, 5)
    number = reservation.on_site_rental(car, return_date)
    assert reservation._rent == {number: car}


def test_cancel_reservation_after_change_reservation():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 30)
    return_date = datetime(2021, 2, 2)
    number = reservation.new_reservation(car, rental_date, return_date)
    new_rental_date = datetime(2021, 2, 1)
    new_return_date = datetime(2021, 2, 6)
    result = reservation.change_reservation(number, new_rental_date,
                                            new_return_date)
    assert result is True
    assert car.rental_dates() == {number: (new_rental_date, new_return_date)}
    assert reservation.cancel_reservation(number) is True
    assert car.rental_dates() == {}
    assert reservation.reservation() == {}


def test_cancel_missed_bookings():
    car = Car("toyota", "rv4", "disel", '5', '5', '5')
    reservation = RentAndReservation('reservation_number.pickle')
    rental_date = datetime(2021, 1, 5)
    return_date = datetime(2021, 1, 20)
    reservation_number = 0
    reservation._reservation[reservation_number] = car
    car.set_rental_dates(reservation_number, rental_date, return_date)
    reservation_numbers = reservation.cancel_missed_bookings()
    assert reservation_numbers == [reservation_number]
