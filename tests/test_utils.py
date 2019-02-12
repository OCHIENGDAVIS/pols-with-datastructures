"""A module for testing utility and helper functions"""
from tests.base_testcase import BaseTest
from app.api.v1.models .party_models import Party, parties
from app.api.v1.models .office_models import Office, offices
from app.api.v1.utils import check_json, ValidateUserInput


class Utils(BaseTest):

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

    def test_check_json(self):
        data = self.party_test_data
        self.assertTrue(check_json(data))

    def test_check_json_empty_data(self):
        self.party_test_data = {}
        data = self.party_test_data
        self.assertFalse(check_json(data))

    def test_check_id_not_int(self):
        self.assertFalse(ValidateUserInput.check_id("1"))
        self.assertTrue(ValidateUserInput.check_id(1))

    def test_check_string_types(self):
        self.assertTrue(ValidateUserInput.check_string_types("my string"))
        self.assertFalse(ValidateUserInput.check_string_types(123))
