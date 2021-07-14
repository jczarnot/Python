from findVehicle import FindVechicle
from vehicle import Car, Boat


def test_split_data_by_brand():
    brands = {}
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '5', '5', '5')
    find_vehicle = FindVechicle()
    brands = find_vehicle.split_data(car1.brand(), car1, brands)
    brands = find_vehicle.split_data(car2.brand(), car2, brands)
    assert brands == {'toyota': [car1], "audi": [car2]}


def test_split_data_by_model():
    models = {}
    boat1 = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat2 = Boat("honda", "b45", "disel", '5', '500', '200', '3')
    find_vehicle = FindVechicle()
    models = find_vehicle.split_data(boat1.model(), boat1, models)
    models = find_vehicle.split_data(boat2.model(), boat2, models)
    assert models == {'b40': [boat1], "b45": [boat2]}


def test_split_data_by_engine():
    engines = {}
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '5', '5', '5')
    find_vehicle = FindVechicle()
    engines = find_vehicle.split_data(car1.engine(), car1, engines)
    engines = find_vehicle.split_data(car2.engine(), car2, engines)
    assert engines == {'disel': [car1, car2]}


def test_split_data_by_fuel_consumption():
    fuel_consumption = {}
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '5', '5', '5')
    find_vehicle = FindVechicle()
    fuel_consumption = find_vehicle.split_data(car1.fuel_consumption(), car1,
                                               fuel_consumption)
    fuel_consumption = find_vehicle.split_data(car2.fuel_consumption(), car2,
                                               fuel_consumption)
    assert fuel_consumption == {'5': [car1, car2]}


def test_split_data_by_doors():
    doors = {}
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '5', '5', '6')
    find_vehicle = FindVechicle()
    doors = find_vehicle.split_data(car1.doors(), car1, doors)
    doors = find_vehicle.split_data(car2.doors(), car2, doors)
    assert doors == {'5': [car1], '6': [car2]}


def test_split_data_by_passangers():
    passangers = {}
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '5', '6', '6')
    find_vehicle = FindVechicle()
    passangers = find_vehicle.split_data(car1.passengers(), car1, passangers)
    passangers = find_vehicle.split_data(car2.passengers(), car2, passangers)
    assert passangers == {'5': [car1], '6': [car2]}


def test_split_data_by_width():
    width = {}
    boat1 = Boat("honda", "b40", "disel", '5', '500', '200', '3')
    boat2 = Boat("honda", "b45", "disel", '5', '500', '200', '3')
    find_vehicle = FindVechicle()
    width = find_vehicle.split_data(boat1.width(), boat1, width)
    width = find_vehicle.split_data(boat2.width(), boat2, width)
    assert width == {'500': [boat1, boat2]}


def test_split_data_by_length():
    length = {}
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("honda", "b45", "disel", '5', '500', '200', '3')
    find_vehicle = FindVechicle()
    length = find_vehicle.split_data(boat1.length(), boat1, length)
    length = find_vehicle.split_data(boat2.length(), boat2, length)
    assert length == {'205': [boat1], '200': [boat2]}


def test_split_data_by_cabins():
    cabins = {}
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("honda", "b45", "disel", '5', '500', '200', '4')
    find_vehicle = FindVechicle()
    cabins = find_vehicle.split_data(boat1.number_of_cabins(), boat1, cabins)
    cabins = find_vehicle.split_data(boat2.number_of_cabins(), boat2, cabins)
    assert cabins == {'3': [boat1], '4': [boat2]}


def test_refining_search_by_cabins_brands_and_models():
    boat1 = Boat("honda", "b40", "disel", '5', '500', '205', '3')
    boat2 = Boat("suzuki", "b45", "disel", '5', '500', '200', '3')
    boat3 = Boat("honda", "b45", "disel", '5', '500', '205', '3')
    boat4 = Boat("suzuki", "b45", "disel", '5', '500', '200', '4')
    boats = [boat1, boat2, boat3, boat4]
    find_vehicle = FindVechicle()
    user_answer = 6  # 6 means searching by numbers of cabins
    vehicle_type = 1  # 1 means boats
    user_choice = '3'
    new_boats_lst = find_vehicle.split_vehicle(boats, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat1, boat2, boat3]
    user_answer = 0  # 0 means searching by brands
    vehicle_type = 1  # 1 means boats
    user_choice = 'honda'
    new_boats_lst = find_vehicle.split_vehicle(new_boats_lst, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat1, boat3]
    user_answer = 1  # 1 means searching by models
    vehicle_type = 1  # 1 means boats
    user_choice = 'b45'
    new_boats_lst = find_vehicle.split_vehicle(new_boats_lst, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat3]


def test_refining_search_by_engines_widths_and_lengths():
    boat1 = Boat("honda", "b40", "lpg", '5', '500', '200', '3')
    boat2 = Boat("suzuki", "b45", "disel", '5', '500', '200', '3')
    boat3 = Boat("honda", "b45", "lpg", '5', '500', '205', '3')
    boat4 = Boat("suzuki", "b45", "disel", '5', '500', '200', '4')
    boats = [boat1, boat2, boat3, boat4]
    find_vehicle = FindVechicle()
    user_answer = 2  # 2 means searching by type of engine
    vehicle_type = 1  # 1 means boats
    user_choice = 'lpg'
    new_boats_lst = find_vehicle.split_vehicle(boats, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat1, boat3]
    user_answer = 4  # 4 means searching by width
    vehicle_type = 1  # 1 means boats
    user_choice = '500'
    new_boats_lst = find_vehicle.split_vehicle(new_boats_lst, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat1, boat3]
    user_answer = 5  # 5 means searching by lengths
    vehicle_type = 1  # 1 means boats
    user_choice = '205'
    new_boats_lst = find_vehicle.split_vehicle(new_boats_lst, user_answer,
                                               vehicle_type, user_choice)
    assert new_boats_lst == [boat3]


def test_refining_search_by_fuel_consumption_and_passangers():
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '3', '6', '6')
    car3 = Car("toyota", "rv4", "disel", '3', '5', '5')
    car4 = Car("audi", "rv4", "disel", '5', '6', '6')
    cars = [car1, car2, car3, car4]
    find_vehicle = FindVechicle()
    user_answer = 3  # 3 means searching by fuel_consumption
    vehicle_type = 0  # 0 means cars
    user_choice = '5'
    cars = find_vehicle.split_vehicle(cars, user_answer, vehicle_type,
                                      user_choice)
    assert cars == [car1, car4]
    user_answer = 4  # 4 means searching by number of passangers
    vehicle_type = 0  # 0 means cars
    user_choice = '6'
    cars = find_vehicle.split_vehicle(cars, user_answer, vehicle_type,
                                      user_choice)
    assert cars == [car4]


def test_no_car_of_the_given_value():
    car1 = Car("toyota", "rv4", "disel", '5', '5', '5')
    car2 = Car("audi", "rv4", "disel", '3', '6', '6')
    car3 = Car("toyota", "rv4", "disel", '3', '5', '5')
    car4 = Car("audi", "rv4", "disel", '5', '6', '6')
    cars = [car1, car2, car3, car4]
    find_vehicle = FindVechicle()
    user_answer = 2  # 2 means searching by type of engine
    vehicle_type = 0  # 0 means cars
    user_choice = 'lpg'
    cars = find_vehicle.split_vehicle(cars, user_answer, vehicle_type,
                                      user_choice)
    assert cars is None
