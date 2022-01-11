ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "status": "Admitted",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "status": "Admitted",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "status": "Admitted",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_animals():
    """Returns all the animal dictionaries in the ANIMALS list

    Returns:
        list: The ANIMAL list containing dictionaries of animals
    """
    return ANIMALS

# Function with a single parameter


def get_single_animal(id):
    """Gives us back the animal dictionary with the corresponding id

    Args:
        id (int): The id of the animal dictionary we want to GET from the API

    Returns:
        dictionary: the dictionary with the corresponding id we passed into the function call
    """
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    """Creates a new animal dictionary and appends it to the ANIMALS list

    Args:
        animal (dictionary): the animal dictionary we want to POST to the API

    Returns:
        dictionary: the animal dictionary we passed into the function
    """
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    """DELETES the animal with the corresponding id

    Args:
        id (int): the id of the animal dictionary we want to DELETE from the ANIMALS list
    """
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    """updates an existing animal dictionary

    Args:
        id (int): the id of the animal dictionary we want to alter
        new_animal (dictionary): the new animal with the updated key:value pairs
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
