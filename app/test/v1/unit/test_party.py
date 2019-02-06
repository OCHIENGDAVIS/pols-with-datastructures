import json
from unittest import TestCase
from app.api.v1.models.party_model import Party
from app.api.v1.models.office_model import Office
from app.api.v1.utils import find_by_id
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
            self.assertEqual(response.status_code, 200, msg="party was not found")

    def test_edit_party(self):
        """Tests that the API edit a party endpoint can edit a party"""
        with self.app.test_client() as c:
            data = dict(
                id=1,
                name="Jubilee",
                hqAddress="Jubilee House",
                logoUrl="https:www.jubilee.co.ke/logo.png"
            )
            c.post("/api/v1/parties", data=json.dumps(data), content_type="application/json")
            new_data = json.dumps(dict(
                name = "New party name"
            ))
            response =c.patch("/api/v1/parties/1/name", data=new_data, content_type="application/json")
            self.assertEqual(response.status_code, 200, msg="party edit failed")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status" , response_msg)
            self.assertEqual(response_msg["status"], 200)
            expected_party_data = response_msg["data"]
            self.assertListEqual(expected_party_data, [{"id":1, "name":"New party name"}])

    def test_delete_party(self):
        """Tests the delete part endpoint of the API"""
        with self.app.test_client() as c:
            data = dict(
                id=1,
                name="Jubilee",
                hqAddress="Jubilee House",
                logoUrl="https:www.jubilee.co.ke/logo.png"
            )
            c.post("/api/v1/parties", data=json.dumps(data), content_type="application/json")
            response = c.delete("/api/v1/parties/1")
            self.assertEqual(response.status_code, 200)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            response_data = response_msg["data"]
            self.assertListEqual(response_data, [{
                            "message": "party deleted successfully"
                        }])

    def test_invalid_delete(self):
        """Tests for deleting a party that is noe their"""
        with self.app.test_client() as c:
            response = c.delete("/api/v1/parties/10")
            self.assertEqual(response.status_code, 404)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            response_data = response_msg["data"]
            self.assertListEqual(response_data, [{
                "message": "party does not exists"
            }])


class TestOffice(TestCase):

    def setUp(self):
        self.app =create_app(config)
        self.office =Office(1, "local government", "office of the MCA")

    def test_init_method(self):
        self.assertEqual(self.office.id, 1)
        self.assertEqual(self.office.type, "local government")
        self.assertEqual(self.office.name, "office of the MCA")

    def test_create_office(self):
        """Tests the creating of a new office"""
        data = dict(
            id=1,
            type="Local government",
            name="Office of the MCA",
        )
        with self.app.test_client() as c:
            response = c.post("/api/v1/offices", data=json.dumps(data), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(response_msg['status'], 201)
            self.assertListEqual(response_msg['data'], [{'id': 1, 'type': "Local government", "name": "Office of the MCA"}])


    def test_office_already_exists(self):
        data = dict(
            id=1,
            type="Local government",
            name="Office of the MCA",
        )
        with self.app.test_client() as c:
            c.post("/api/v1/offices", data=json.dumps(data), content_type="application/json")
            new_post = c.post("/api/v1/offices", data=json.dumps(data), content_type="application/json")
            self.assertEqual(new_post.status_code, 400)
            response_msg = json.loads(new_post.data.decode("UTF-8"))
            self.assertEqual(response_msg["message"], "Office with that ID already exists")


    def test_get_all_parties(self):
        with self.app.test_client() as c:
            response = c.get("/api/v1/parties")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")











     


        



