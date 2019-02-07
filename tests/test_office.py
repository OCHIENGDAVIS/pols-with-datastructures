import json
# from tests.base_testcase import BaseTest
from tests.base_testcase import BaseTest
from app.api.v1.models.office_models import Office


class TestOffice(BaseTest):

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
        with self.app_context():
            response = self.app.post("/api/v1/offices", data=json.dumps(self.office_test_data),
                                     content_type="application/json")
            self.assertEqual(response.status_code, 400)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual(
                response_msg["message"], "Office with that ID already exists")
