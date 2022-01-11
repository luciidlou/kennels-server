CUSTOMERS = [
    {
        "id": 15,
        "name": "Ryan Tanay",
        "email": "ryan@tanay.com",
    },
    {
        "id": 16,
        "name": "Emma Beaton",
        "email": "emma@beaton.com",
    },
    {
        "id": 17,
        "name": "Dani Adkins",
        "email": "dani.adkins.com",
    },
    {
        "id": 18,
        "name": "Adam Oswalt",
        "email": "adam@oswalt.com",
    },
    {
        "id": 19,
        "name": "Fletcher Bangs",
        "email": "flangs@bangs.com",
    },
    {
        "id": 20,
        "name": "Angela Lee",
        "email": "lee@lee.com",
    },
    {
        "id": 21,
        "name": "mike mike",
        "email": "m@m.com",
    },
    {
        "id": 22,
        "name": "Jimmy  Neutron",
        "email": "jimmy@brainblast.com",
    },
    {
        "id": 23,
        "name": "Marty Robbins",
        "email": "marty@bigiron.com",
    },
    {
        "id": 25,
        "name": "John  Steinbeck",
        "email": "john@steinbeck.com",
    }
]


def get_all_customers():
    """Returns all the customer dictionaries in the CUSTOMERS list

    Returns:
        list: The CUSTOMER list containing dictionaries of customers
    """
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    """Gives us back the customer dictionary with the corresponding id

    Args:
        id (int): The id of the customer dictionary we want to GET from the API

    Returns:
        dictionary: the dictionary with the corresponding id we passed into the function call
    """

    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    """Creates a new customer dictionary and appends it to the CUSTOMERS list

    Args:
        customer (dictionary): the customer dictionary we want to POST to the API

    Returns:
        dictionary: the customer dictionary we passed into the function
    """
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def delete_customer(id):
    """DELETES the customer with the corresponding id

    Args:
        id (int): the id of the customer dictionary we want to DELETE from the CUSTOMERS list
    """
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """updates an existing customer dictionary

    Args:
        id (int): the id of the customer dictionary we want to alter
        new_customer (dictionary): the new customer with the updated key:value pairs
    """
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
