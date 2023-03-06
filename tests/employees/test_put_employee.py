import string
import random

from tests.clients.clients_bundle import employee_client
from tests.configuration import ROLE_ENUM


def test_positive():
    name = "test_" + "".join(random.sample(string.ascii_letters, 5))
    role = random.choice(ROLE_ENUM)
    employee_id = random.choice([1, 2, 3])
    response = employee_client.put_employee(name, role, employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"