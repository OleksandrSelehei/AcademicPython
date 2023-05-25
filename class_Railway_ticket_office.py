import asyncio


class Train:
    auto_increment = 0

    # initialization
    def __init__(self, number, route, departure_time, seat_number):
        Train.auto_increment += 1
        self.id = Train.auto_increment
        self.number = number
        self.route = route
        self.departure_time = departure_time
        self.seat_number = seat_number

        # Text output

    def __str__(self):
        return f"Потяг {self.id} -> {self.number}, {self.route}, {self.departure_time}"


class Stop:
    # initialization
    def __init__(self, station, arrival_time, departure_time):
        self.station = station
        self.arrival_time = arrival_time
        self.departure_time = departure_time


class Route:
    # initialization
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops


class Ticket:
    # initialization
    def __init__(self, passenger_name, passenger_surname, train, carriage_number, seat_number, departure_station,
                 arrival_station, departure_date):
        self.passenger_name = passenger_name
        self.passenger_surname = passenger_surname
        self.train = train
        self.carriage_number = carriage_number
        self.seat_number = seat_number
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_date = departure_date


class TicketOffice:
    # initialization
    def __init__(self, trains, routes):
        self.trains = trains
        self.routes = routes
        self.tickets = []

    # output of all existing trains
    def search(self):
        for train in self.trains:
            print(train)

    async def sell_ticket(self, passenger_name, passenger_surname, train_number, carriage_number, seat_number,
                          departure_station, arrival_station, departure_date):
        # checking if the given train exists
        train = next((train for train in self.trains if train.number == train_number), None)
        if train is None:
            print(f"Error: Train {train_number} not found")
            return

        # checking if the given route exists
        route = next((route for route in self.routes if route.name == train.route), None)
        if route is None:
            print(f"Error: Route {train.route} not found")
            return

        # checking for ticketing exceptions
        try:
            seat = next((seat for seat in train.seat_number if seat_number == seat), None)
            if seat is None:
                raise ValueError(
                    f"sorry, unfortunately it is not possible to create such a ticket for sale because the train number {train.number} seat number {seat_number} has already been sold to the ticket.")
            train.seat_number.remove(seat)
        except ValueError as error:
            print(f"Error: {error}")
            return

        # Checking departure and stop locations
        departure_stop = next((stop for stop in route.stops if stop.station == departure_station), None)
        arrival_stop = next((stop for stop in route.stops if stop.station == arrival_station), None)
        if departure_stop is None:
            print(f"Error: Station {departure_station} is not in route {route.name}")
            return
        if arrival_stop is None:
            print(f"Error: Station {arrival_station} is not in route {route.name}")
            return

        # Creating a ticket and adding it to the archive to expand the functionality of the program
        ticket = Ticket(passenger_name, passenger_surname, train, carriage_number, seat, departure_station,
                        arrival_station, departure_date)
        self.tickets.append(ticket)
        print(
            f"Name: {ticket.passenger_name}\t\t\t\t\t\tData: {ticket.departure_date}\nSurname: {ticket.passenger_surname}\t\t\t\t\tTrain: {ticket.train}\nDeparture station: {ticket.departure_station}\t\t\tNumber carriage: {ticket.carriage_number}\nArrival station: {ticket.arrival_station}\t\t\t\tNumber seat: {ticket.seat_number}")
        print("\nThe ticket was sold successfully")


async def work_office():
    # Creating a list with train class objects
    trains_ = [Train("12345", "A-B-C", "10:30", [1, 2, 4, 5, 6]), Train("21345", "B-C-D", "11:30", [1, 3, 4, 5, 6, 8]),
               Train("42356", "A-B-D", "12:00", [4, 5, 9])]
    # Creation of a list with objects classes route
    routes_ = [Route("A-B-C", [Stop("A", "10:00", "10:30"), Stop("B", "12:30", "12:45"), Stop("C", "15:30", "--:--")]),
               Route("B-C-D", [Stop("B", "11:00", "11:30"), Stop("C", "15:30", "15:45"), Stop("D", "19:30", "--:--")]),
               Route("A-B-D", [Stop("A", "11:30", "12:00"), Stop("B", "16:30", "16:45"), Stop("D", "21:00", "--:--")])]

    # Working with the program
    ticket_office = TicketOffice(trains_, routes_)

    ticket_1 = ticket_office.sell_ticket("Johna", "Doe", "21345", "8", 6, "B", "D", "3/16/23")
    ticket_2 = ticket_office.sell_ticket("John", "Doe", "42356", "8", 5, "A", "D", "3/16/23")
    ticket_3 = ticket_office.sell_ticket("John", "Doe", "42356", "8", 5, "A", "D", "3/16/23")

    print("-" * 50)
    # Creating an object of the cash register class
    print("List of all trains:")
    # output of all existing trains
    print(ticket_office.search())
    print("-" * 50)
    print("Ticket")
    # output of all data verification and ticket sale True
    await ticket_1
    print("-" * 50)
    # output of all data verification and ticket sale False
    await ticket_2
    print("-" * 50)
    await ticket_3

asyncio.run(work_office())
