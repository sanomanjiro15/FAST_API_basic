from tests.checkers.general import CheckerGeneral
from tests.clients.clients_bundle import employee_client
import random


def test_positive():
    employee_id = random.choice([1, 2, 3])

    response = employee_client.get_employee_by_id(employee_id)
    assert response.status_code == 200, "Статус код не соответствует ожидаемому"
    assert CheckerGeneral().validate_items(response.json(), "schemas/employees.json")