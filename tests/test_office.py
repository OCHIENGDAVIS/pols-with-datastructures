"""A module to test all the office functionalities"""

import json
from tests.base_testcase import BaseTest
from app.api.v1.models.office_models import Office


class TestOffice(BaseTest):
    """""The main class for testing office endpoints"""

    def test_init_method(self):
        office = Office(1, "County", "Office of MCA")
        self.assertEqual(office.id, 1)
        self.assertEqual(office.type, "County")
        self.assertEqual(office.name, "Office of MCA")

    def test_create_office(self):
        """Tests the creating of a new office"""
        with self.app_context():
            response = self.app.post(
                "/api/v1/offices", data=json.dumps(self.office_test_data), content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(response_msg['status'], 201)
            self.assertListEqual(response_msg['data'], [
                                 {"id": 1, "name": "Office of the MCA"}])

    def test_create_office_already_exists(self):
        """Tests for creating of an office that already exists"""
        with self.app_context():
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertListEqual(
                response_msg["data"], [{
                    "message": "Check the data you are trying to send please"
                }])

    def test_get_office(self):
        """Tests the getting of all offices"""
        with self.app_context():
            response = self.app.get("/api/v1/offices/1")
            self.assertEqual(response.status_code, 200,
                             msg="Error office did not return 200 OK")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertListEqual(response_msg["data"], [{
                "id": 1,
                "name": "Office of the MCA"
            }])

    def test_get_office_not_found(self):
        """Tests the getting of an office that do not exists"""
        with self.app_context():
            response = self.app.get("/api/v1/offices/1000")
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertListEqual(response_msg["data"], [{
                "message": "Please try and check the data you are trying to send "
            }])

    def test_get_all_offices(self):
        """Tests the getting of all offices"""
        with self.app_context():
            response = self.app.get("/api/v1/offices")
            self.assertEqual(response.status_code, 200)
