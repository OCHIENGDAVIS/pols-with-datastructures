"""A module for testing utility and helper functions"""
from tests.base_testcase import BaseTest
from app.api.v1.utils import validate_party_info
from app.api.v1.models .party_models import Party, parties
from app.api.v1.models .office_models import Office, offices


class Utils(BaseTest):
    """Main class for testing utility functions"""

    def test_validate_party_info_data_is_none(self):
        """Tests whether a post request with no body is allowed """
        self.party_test_data = {}
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "party data must be provided", "code": 400})

    def test_validate_party_info_id_is_none(self):
        """Tests whether creating a party with no id is allowed"""
        self.party_test_data["id"] = None
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "id is required", "code": 400})

    def test_validate_party_info_name_is_none(self):
        """Tests for creating a party with no name"""
        self.party_test_data["name"] = None
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "name is required", "code": 400})

    def test_validate_party_info_id_is_string(self):
        """Tests for creating a party with a string id"""
        self.party_test_data["id"] = "1"
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "id must be a number", "code": 400})

    def test_validate_party_info_name_is_empty_string(self):
        """Tests for creating a party with an empty name"""
        self.party_test_data["name"] = ""
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "name can not be an empty string", "code": 400})

    def test_validate_party_info_hqaddress_is_none(self):
        """Tests creating a party with no head quater address"""
        self.party_test_data["hqAddress"] = None
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response,
            {"message": "hqAddress is required", "code": 400})

    def test_validate_party_info_logourl_is_none(self):
        """Tests creating a party with no logo url"""
        self.party_test_data["logoUrl"] = None
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "party logo Url is required", "code": 400})

    def test_validate_party_info_logourl_not_a_string(self):
        """Tests creating a party with an integer logourl"""
        self.party_test_data["logoUrl"] = 12
        response = validate_party_info(self.party_test_data)
        self.assertDictEqual(
            response, {"message": "logo must be a string", "code": 400})

    def test_create_party_class_method(self):
        """Tests the create party class method of the Party class"""
        new_party = Party.create_party(self.party_test_data["id"], self.party_test_data["name"],
                                       self.party_test_data["hqAddress"], self.party_test_data["logoUrl"])
        self.assertDictEqual(new_party, parties[len(parties) - 1])

    def test_create_office_class_method(self):
        """Tests the create office class method of the Office class"""
        new_office = Office.create_office(self.office_test_data["id"], self.office_test_data["type"],
                                          self.office_test_data["name"])
        self.assertDictEqual(new_office, offices[len(offices) - 1])
