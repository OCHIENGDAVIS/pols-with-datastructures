offices = []


class Office:
    """A method to initialize the office resource"""

    def __init__(self, office_id, office_type, office_name):
        self.id = office_id
        self.type = office_type
        self.name = office_name

    @classmethod
    def create_office(cls, office_id, office_type, office_name):
        """A method to create a new office"""
        new_offfice = {
            "id": office_id,
            "type": office_type,
            "name": office_name
        }
        offices.append(new_offfice)
        return new_offfice
