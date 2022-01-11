EMPLOYEES = [
    {
        "id": 1,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com",
        "location_id": 1
    },
    {
        "id": 2,
        "name": "Zoe LeBlanc",
        "location_id": 1,
        "email": "zoe@leblanc.com"
    },
    {
        "id": 3,
        "name": "Meg Ducharme",
        "location_id": 2,
        "email": "meg@ducharme.com"
    },
    {
        "id": 5,
        "name": "Hannah Hall",
        "location_id": 2,
        "email": "hannah@hall.com"
    },
    {
        "id": 9,
        "name": "Caitlin Stein",
        "location_id": 2,
        "email": "caitlin@stein.com"
    },
    {
        "id": 10,
        "name": "Greg Korte",
        "location_id": 1,
        "email": "greg@korte.com"
    },
    {
        "id": 11,
        "name": "Charisse Lambert",
        "location_id": 1,
        "email": "charisse@lambert.com"
    },
    {
        "id": 14,
        "name": "Jenna Solis",
        "location_id": 2,
        "email": "jenna@solis.com"
    },

    {
        "id": 24,
        "name": "Bobby Light",
        "location_id": 2,
        "email": "bobby@light.com"
    },
    {
        "id": 26,
        "name": "Freddy Newandyke",
        "location_id": 1,
        "email": "mrorange@reservoir.com"
    }
]


def get_all_employees():
    """Returns all the employee dictionaries in the EMPLOYEES list

    Returns:
        list: The EMPLOYEE list containing dictionaries of employees
    """
    return EMPLOYEES

# Function with a single parameter


def get_single_employee(id):
    """Gives us back the employee dictionary with the corresponding id

    Args:
        id (int): The id of the employee dictionary we want to GET from the API

    Returns:
        dictionary: the dictionary with the corresponding id we passed into the function call
    """
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """Creates a new employee dictionary and appends it to the EMPLOYEES list

    Args:
        employee (dictionary): the employee dictionary we want to POST to the API

    Returns:
        dictionary: the employee dictionary we passed into the function
    """
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_employee(id):
    """DELETES the employee with the corresponding id

    Args:
        id (int): the id of the employee dictionary we want to DELETE from the EMPLOYEES list
    """
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """updates an existing employee dictionary

    Args:
        id (int): the id of the employee dictionary we want to alter
        new_employee (dictionary): the new employee with the updated key:value pairs
    """
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break
