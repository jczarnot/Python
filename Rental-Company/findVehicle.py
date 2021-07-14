class FindVechicle:

    def split_data(self, attribute, vehicle, vehicles_dict):
        '''
        Checks if the received attribute is already a key in the given
        dictionary,if it does not create it and assigns it a list that will
        contain all vehicles that have the same attribute,
        if it already exists, adds the vehicle to the list associated with it
        '''
        if attribute in vehicles_dict.keys():
            vehicles_dict[attribute].append(vehicle)
        else:
            vehicles_dict[attribute] = [vehicle]
        return vehicles_dict

    def split_vehicle(self, vehicles_lst, user_answer, vehicle_type,
                      user_choice):
        '''
        Splits the list of vehicles according to the attribute
        selected by the user and returns the list of vehicles
        that have this attribute
        '''
        self.vehicles_dict = {}
        if vehicles_lst is not None:
            for vehicle in vehicles_lst:
                if user_answer == 0:  # brand
                    self.split_data(vehicle.brand(), vehicle,
                                    self.vehicles_dict)
                if user_answer == 1:  # model
                    self.split_data(vehicle.model(), vehicle,
                                    self.vehicles_dict)
                if user_answer == 2:  # engine
                    self.split_data(vehicle.engine(), vehicle,
                                    self.vehicles_dict)
                if user_answer == 3:  # fuel_consumption
                    self.split_data(vehicle.fuel_consumption(), vehicle,
                                    self.vehicles_dict)
                if vehicle_type == 0 or vehicle_type is None:
                    if user_answer == 4:  # passengers
                        self.split_data(vehicle.passengers(), vehicle,
                                        self.vehicles_dict)
                    if user_answer == 5:  # doors
                        self.split_data(vehicle.doors(), vehicle,
                                        self.vehicles_dict)
                if vehicle_type == 1 or vehicle_type is None:
                    if user_answer == 4:  # width
                        self.split_data(vehicle.width(), vehicle,
                                        self.vehicles_dict)
                    if user_answer == 5:  # length
                        self.split_data(vehicle.length(), vehicle,
                                        self.vehicles_dict)
                    if user_answer == 6:  # number of cabins
                        self.split_data(vehicle.number_of_cabins(), vehicle,
                                        self.vehicles_dict)
        if self.vehicles_dict.get(user_choice):
            self.new_vehicle_lst = self.vehicles_dict[user_choice]
            return self.new_vehicle_lst
