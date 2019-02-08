"""A module to test all the office functionalities"""

import json
from tests.base_testcase import BaseTest
from app.api.v1.models.office_models import Office


class TestOffice(BaseTest):
    """""The main class for testing office endpoints"""

    def test_create_office(self):
        """Tests the creating of a new office"""
        with self.app_context():
            response = self.app.post(
                "/api/v1/offices", data=json.dumps(self.office_test_data), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(response_msg['status'], 201)
            self.assertListEqual(response_msg['data'], [
                                 {'id': 1, 'type': "Local government", "name": "Office of the MCA"}])

    def test_create_office_already_exists(self):
        """Tests for creating of an office that already exists"""
        with self.app_context():
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Office with that ID already exists")

    def test_get_office(self):
        """Tests the getting of all offices"""
        with self.app_context():
            response = self.app.get("/api/v1/offices/1")
            self.assertEqual(response.status_code, 200,
                             msg="Error office did not return 200 OK")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertListEqual(response_msg["data"], [{
                "id": 1,
                "type": "Local government",
                "name": "Office of the MCA"
            }])

    def test_get_office_not_found(self):
        """Tests the getting of an office that do not exists"""
        with self.app_context():
            response = self.app.get("/api/v1/offices/1000")
            self.assertEqual(response.status_code, 404,
                             msg="Error get office not found dir not return 404")

    def test_create_office_no_data(self):
        """Tests the creation of an office with no data"""
        with self.app_context():
            self.office_test_data = {}
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "You must provide data to create the office")

    def test_create_office_id_none(self):
        """Tests the creation of an office with no id"""
        with self.app_context():
            self.office_test_data["id"] = None
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Id is required")

    def test_create_office_type_none(self):
        """Tests the creation of an office with no office type"""
        with self.app_context():
            self.office_test_data["type"] = None
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Type required")

    def test_create_office_name_none(self):
        """Tests the creation of an office with no name"""
        with self.app_context():
            self.office_test_data["name"] = None
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Name is required")

    def test_create_office_name_not_string(self):
        """Tests the creation of an office with an interger name"""
        with self.app_context():
            self.office_test_data["name"] = 123
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Office name must be a string")

    def test_create_office_id_not_integer(self):
        """Tests the creation of an office with an Id not an integer"""
        with self.app_context():
            self.office_test_data["id"] = "this should be  interger id"
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Office id must be an integer")

    def test_get_all_offices(self):
        """Tests the getting of all offices"""
        with self.app_context():
            response = self.app.get("/api/v1/offices")
            self.assertEqual(response.status_code, 200)
