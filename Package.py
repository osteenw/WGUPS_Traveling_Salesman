class Package:
    def __init__(self, id, address, deadline, city, state, zip, weight, notes, status):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.notes = notes
        self.status = status

    def values(self):
        return [self.address, self.deadline, self.city, self.state, self.zip, self.weight, self.status]
