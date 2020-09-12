#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # ========= create empty list and then fill a dictionary with each tickets source and destination =========
    route = [None] * length
    location_dict = dict()

    for ticket in tickets:
        location_dict[ticket.source] = ticket.destination
        
    # ========= set the first destination using the ticket with "None" source =========
    next_route = location_dict["NONE"]
    
    # ========= search for each ticket's next route then add it to the route array until the next route is "None" =========
    for i in range(0, length):
        route[i] = next_route
        next_route = location_dict[next_route]

    return route
