import json
from unittest import TestCase
from app.api.v1.models.party_model import Party, parties
from app.api.v1.utils import find_by_id, find_by_name
from app.main import create_app
from app.instance import config

class TestParty(TestCase):
    def setUp(self):
        self.app = create_app(config)
        self.party = Party(1, "NASA", "Capital Hill", "https://www.nasa.co.ke/img/nasa.png")

    def test_init_method(self):
        """Tests the Party Constructor"""
        self.assertEqual(self.party.id, 1)
        self.assertEqual(self.party.name, 'NASA')
        self.assertEqual(self.party.hqAddress, 'Capital Hill')
        self.assertEqual(self.party.logoUrl, 'https://www.nasa.co.ke/img/nasa.png')

    def test_create_party(self):
        """Tests the creating of a party"""
        data = dict(
            id=1,
            name="Jubilee",
            hqAddress="Jubilee House",
            logoUrl = "https:www.jubilee.co.ke/logo.png"
        )
        with self.app.test_client() as c:
            response = c.post("/api/v1/parties", data=json.dumps(data), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(response_msg['status'], 201)
            self.assertListEqual(response_msg['data'], [{'id':1, 'name': "Jubilee"}])



    def test_party_exists_after_creation(self):
        """Tests whether a party exists after creating it"""
        self.party.create_party(self.party.id, self.party.name, self.party.hqAddress,self.party.logoUrl)
        found_party = find_by_id(self.party.id)
        self.assertTrue(found_party, msg="Party did not get created!")


    def test_get_all_parties(self):
        """Test whether the API can list all products"""
        with self.app.test_client() as c:
            response = c.get("/api/v1/parties")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")

    def test_get_specific_party(self):
        """Tests the getting of a specific party"""
        with self.app.test_client() as c:
            response = c.get("/api/v1/parties/1")
            self.assertEqual(response.status_code, 200)
     


        



