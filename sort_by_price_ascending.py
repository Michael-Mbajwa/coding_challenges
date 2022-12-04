import json
from operator import itemgetter

def sort_by_price_ascending(json_string):
    """From my interview from NextGate Tech
    Given a json file, sort the items by price, name in ascending order
    Return the sorted json file as the output

    Args:
        json_string (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    price_dictionary = json.loads(json_string)
    sorted_price_dictionary = sorted(price_dictionary, key=itemgetter("price", "name"))
    
    result = json.dumps(sorted_price_dictionary)
    return result
print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))