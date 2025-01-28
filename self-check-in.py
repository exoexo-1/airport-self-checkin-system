class AirportSelfCheckInMachine:
    def __init__(self):  # Corrected here
        self.boarding_pass_template = """
        -----------------------------------
        | Boarding Pass                    |
        -----------------------------------
        | Flight Number: {flight_number}   |
        | Passenger Name: {passenger_name} |
        | Seat Number: {seat_number}       |
        -----------------------------------
        """
        self.bag_tag_template = """
        -----------------------------------
        | Bag Tag                          |
        -----------------------------------
        | Flight Number: {flight_number}   |
        | Passenger Name: {passenger_name} |
        | Bag ID: {bag_id}                 |
        -----------------------------------
        """
        self.flight_database = {
            "ABC123": {
                "flight_number": "ABC123",
                "destination": "New York",
                "departure_time": "12:00 PM",
                "seat_map": ["A1", "A2", "A3", "A4"],
            },
        }
        self.bag_id_counter = 1

    def start(self):
        print("Welcome to the Airport Self Check-In Machine!")
        self.activate_kiosk()

    def activate_kiosk(self):
        start_activation = input("Press START/ACTIVATE KIOSK to begin: ").strip().upper()
        if start_activation == "START" or start_activation == "ACTIVATE KIOSK":
            self.check_flight_confirmation()
        else:
            print("Invalid input. Please try again.")
            self.activate_kiosk()

    def check_flight_confirmation(self):
        flight_confirmation_number = input("Please input your flight confirmation number: ").strip().upper()
        if flight_confirmation_number in self.flight_database:
            print("Flight confirmation number verified.")
            self.confirmation()
        else:
            print("Invalid flight confirmation number. Please try again.")
            self.check_flight_confirmation()

    def confirmation(self):
        finished_confirmation = input("Are you finished? (yes/no): ").strip().lower()
        if finished_confirmation == "yes":
            self.check_bags()
        elif finished_confirmation == "no":
            self.start()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.confirmation()

    def check_bags(self):
        check_bags_input = input("Would you like to check bags? (yes/no): ").strip().lower()
        if check_bags_input == "yes":
            bag_id = self.generate_bag_id()
            print("Bags checked.")
            self.print_bag_tag(bag_id)
            self.print_boarding_pass()
            print("Thank you for using the Self Check-In Machine. Have a great flight!")
        elif check_bags_input == "no":
            self.print_boarding_pass()
            print("Thank you for using the Self Check-In Machine. Have a great flight!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            self.check_bags()

    def generate_bag_id(self):
        bag_id = f"Bag{self.bag_id_counter}"
        self.bag_id_counter += 1
        return bag_id

    def print_bag_tag(self, bag_id):
        flight_info = self.flight_database["ABC123"]  # Assuming only one flight for simplicity
        passenger_name = input("Please enter your name: ").strip().title()
        print(
            self.bag_tag_template.format(
                flight_number=flight_info["flight_number"],
                passenger_name=passenger_name,
                bag_id=bag_id,
            )
        )

    def print_boarding_pass(self):
        flight_info = self.flight_database["ABC123"]  # Assuming only one flight for simplicity
        passenger_name = input("Please enter your name: ").strip().title()
        available_seats = flight_info["seat_map"]
        seat_number = self.select_seat(available_seats)
        print(
            self.boarding_pass_template.format(
                flight_number=flight_info["flight_number"],
                passenger_name=passenger_name,
                seat_number=seat_number,
            )
        )

    def select_seat(self, available_seats):
        print("Available seats:", available_seats)
        chosen_seat = input("Select your seat number from the available options: ").strip().upper()
        if chosen_seat in available_seats:
            available_seats.remove(chosen_seat)  # Mark seat as taken
            return chosen_seat
        else:
            print("Invalid seat selection. Please choose from the available seats.")
            return self.select_seat(available_seats)


# Usage
self_check_in_machine = AirportSelfCheckInMachine()
self_check_in_machine.start()
