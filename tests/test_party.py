"""A module for testing the all party functionalities"""
import json
from tests.base_testcase import BaseTest
from app.api.v1.models.party_models import Party, parties
from app.api.v1.models.office_models import Office
# from app.api.v1.utils import find_by_id


class TestParty(BaseTest):

    def test_create_party(self):
        """Tests the creating of a party"""
        with self.app_context():
            response = self.app.post(
                "/api/v1/parties", data=json.dumps(self.party_test_data), content_type="application/json")
            self.assertEqual(response.status_code, 201,
                             msg="POST method did not return a 201 created code")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg['status'], 201, msg="status not in response, expected status")
            self.assertListEqual(response_msg['data'], [
                                 {'id': 1, 'name': "Jubilee"}])

    def test_create_party_already_exists(self):
        """Tests the creation of a party that already exists"""
        with self.app_context():
            response = self.app.post(
                "/api/v1/parties", data=json.dumps(self.party_test_data), content_type="application/json")
            self.assertEqual(response.status_code, 400,
                             msg="POST creating an existing party did not return a 400 bad request.")

    def test_get_all_parties(self):
        """Test whether the API can list all products"""
        with self.app_context():
            response = self.app.get("/api/v1/parties")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")

    def test_get_specific_party(self):
        """Tests the getting of a specific party"""
        with self.app_context():
            response = self.app.get("/api/v1/parties/1")
            self.assertEqual(response.status_code, 200,
                             msg="party was not found")

    def test_get_party_not_found(self):
        """Tests the getting of a party which is not there """
        with self.app_context():
            response = self.app.get("/api/v1/parties/1000")
            self.assertEqual(response.status_code, 404,
                             msg="Error Party found, expectedd a 404 not found")

    def test_edit_party(self):
        """Tests that the API edit a party endpoint can edit a party"""
        with self.app_context():
            new_json_payload = json.dumps(dict(
                name="New party name"
            ))
            response = self.app.patch("/api/v1/parties/1/name",
                                      data=new_json_payload, content_type="application/json")
            self.assertEqual(response.status_code, 200,
                             msg="party edit failed")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            self.assertEqual(response_msg["status"], 200)
            expected_party_data = response_msg["data"]
            self.assertListEqual(expected_party_data, [
                                 {"id": 1, "name": "New party name"}])

    def test_delete_party(self):
        """Tests the delete party endpoint of the API"""
        with self.app_context():
            party_to_delete = dict(
                id=4,
                name="Jubilee",
                hqAddress="Jubilee House",
                logoUrl="https:www.jubilee.co.ke/logo.png"
            )
            response = self.app.post(
                "/api/v1/parties", data=json.dumps(party_to_delete), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response = self.app.delete("/api/v1/parties/4")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            response_data = response_msg["data"]
            self.assertListEqual(response_data, [{
                "message": "party deleted successfully"
            }])

    def test_invalid_delete(self):
        """Tests for deleting a party that is not their"""
        with self.app_context():
            response = self.app.delete("/api/v1/parties/10")
            self.assertEqual(response.status_code, 404)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertIn("status", response_msg)
            response_data = response_msg["data"]
            self.assertListEqual(response_data, [{
                "message": "party does not exists"
            }])

    def test_get_all_parties_class_method(self):
        self.assertDictEqual(Party.get_all_parties(), {"parties": parties})
