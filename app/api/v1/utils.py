
def check_json(data):
    if not data:
        return False
    return True


class ValidateUserInput:

    @classmethod
    def check_id(cls, id):
        if not isinstance(id, int) or id < 0:
            return False
        return True

    @classmethod
    def check_string_types(cls, name):
        if not isinstance(name, str) or name == "":
            return False
        return True

    @classmethod
    def find_by_id(cls, _id, item_iterable):
        """A utility funtion to find a particular item in a list by id"""
        for item in item_iterable:
            if item['id'] == _id:
                return item
        return None

    @classmethod
    def item_exists(cls, item_id, item_iterable):
        if next(filter(lambda x: x['id'] == item_id, item_iterable), None):
            return True
        else:
            return False
