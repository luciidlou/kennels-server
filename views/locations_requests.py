LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North"
    },
    {
        "id": 2,
        "name": "Nashville South"
    }
]


def get_all_locations():
    """Returns all the location dictionaries in the LOCATIONS list

    Returns:
        list: The LOCATION list containing dictionaries of locations
    """
    return LOCATIONS

# Function with a single parameter


def get_single_location(id):
    """Gives us back the location dictionary with the corresponding id

    Args:
        id (int): The id of the location dictionary we want to GET from the API

    Returns:
        dictionary: the dictionary with the corresponding id we passed into the function call
    """
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    """Creates a new location dictionary and appends it to the LOCATIONS list

    Args:
        location (dictionary): the location dictionary we want to POST to the API

    Returns:
        dictionary: the location dictionary we passed into the function
    """
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location


def delete_location(id):
    """DELETES the location with the corresponding id

    Args:
        id (int): the id of the location dictionary we want to DELETE from the LOCATIONS list
    """
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    """updates an existing location dictionary

    Args:
        id (int): the id of the location dictionary we want to alter
        new_location (dictionary): the new location with the updated key:value pairs
    """
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break
