
parties = []


class Party:
    """A class representing the party resource of the application"""

    def __init__(self, party_id, name, hqaddress, logourl):
        """Initializes a party object"""
        self.id = party_id
        self.name = name
        self.hqAddress = hqaddress
        self.logoUrl = logourl

    @classmethod
    def create_party(cls, party_id, name, hqadress, logourl):
        """A method to create a party """
        new_party = {
            'id': party_id,
            'name': name,
            'hqAddress': hqadress,
            'logoUrl': logourl
        }
        parties.append(new_party)
        return new_party

    @classmethod
    def get_all_parties(cls):
        """A method to get all parties"""
        return {
            'parties': parties
        }
