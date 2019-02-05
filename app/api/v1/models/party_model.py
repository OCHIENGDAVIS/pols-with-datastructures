
parties = []

class Party:
    def __init__(self, party_id, name, hqaddress, logourl):
        self.id = party_id
        self.name = name
        self.hqAddress = hqaddress
        self.logoUrl = logourl


    @classmethod
    def create_party(cls,party_id ,name, hqadress, logourl):
        new_party = {
            'id': party_id,
            'name':name,
            'hqAddress': hqadress,
            'logoUrl': logourl

        }
        parties.append(new_party)
        return new_party

    @classmethod
    def get_all_parties(cls):
        return {
            'parties': parties
        }