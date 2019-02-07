from app.api.v1.models.party_models import parties


def validate_party_info(party_dict):
    """A utility function to validate party inputs"""
    data = party_dict
    id = data.get("id", None)
    name = data.get('name', None)
    hqAddress = data.get("hqAddress", None)
    logoUrl = data.get("logoUrl", None)
    if id is None:
        return {"message": "id is required", "code": 400}
    elif not isinstance(id, int):
        return {"message": "id must be a number", "code": 400}
    elif name is None:
        return {"message": "name is required", "code": 400}
    elif len(name) < 1:
        return {"message": "name can not be an empty string", "code": 400}
    elif not isinstance(name, str):
        return {"message": "name must be a string", "code": 400}
    elif hqAddress is None:
        return {"message": "hqAddress is required", "code": 400}
    elif len(hqAddress) < 1:
        return {"message": "hqaddress  can not be an empty string", "code": 400}
    elif logoUrl is None:
        return {"message": "party logo Url is required", "code": 400}
    elif len(logoUrl) < 1:
        return {"message": "Logo url  can not be an empty string", "code": 400}
    elif not isinstance(logoUrl, str):
        return {"message": "logo must be a string", "code": 400}
    elif next(filter(lambda x: x['id'] == id, parties), None):
        return {"message": "party with that id already exists", "code": 400}


# def find_by_id(item_id, item_iterable ):
#     if next(filter(lambda x:x['id']== item_id, item_iterable), None):
#         return True
#     else:
#         return False

def find_by_id(_id):
    """A utility funtion to find a particular party by id"""
    for item in parties:
        if item['id'] == _id:
            return True
    return False


def find_item_by_id(item_id, item_iterable):
    """A utility function to find a particular party by name"""
    if next(filter(lambda x: x['id'] == item_id, item_iterable), None):
        return True
    else:
        return False
