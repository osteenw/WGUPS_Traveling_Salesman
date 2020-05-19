class Package:
    def __init__(self, id, address, deadline, city, state, zip, weight, status, notes):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.notes = notes

    def values(self):
        return [self.address, self.deadline, self.city, self.state, self.zip, self.weight, self.status]
