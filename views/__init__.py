from .animal_requests import (create_animal, delete_animal, get_all_animals,
                              get_animals_by_location_id, get_animal_by_status,
                              get_single_animal, update_animal)
from .customers_requests import (create_customer, delete_customer,
                                 get_all_customers, get_customers_by_email,
                                 get_single_customer, update_customer)
from .employees_requests import (create_employee, delete_employee,
                                 get_all_employees,
                                 get_employees_by_location_id,
                                 get_single_employee, update_employee)
from .locations_requests import (create_location, delete_location,
                                 get_all_locations, get_single_location,
                                 update_location)
