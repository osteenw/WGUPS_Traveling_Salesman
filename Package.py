class Package:
    def __init__(self, id, address_id, address, deadline, city, state, zip, weight, status, notes):
        self.id = id
        self.address_id = address_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = status
        self.notes = notes

    def package_string(self):
        string = "Package ID: {id:02d} | Deadline: {deadline:9s} | {status:18s} | Weight: {weight:2s} kilos |" \
                 " {city:16s} | {state:2s} | {zip:5s} | {address:20s} |  {notes}" \
            .format(id=self.id, deadline=self.deadline, status=self.status, state=self.state, city=self.city,
                    zip=self.zip, address=self.address, weight=self.weight, notes=self.notes)
        return string
