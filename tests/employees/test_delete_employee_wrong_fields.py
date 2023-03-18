#моя задача
import pytest


@pytest.mark.parametrize("employee_id", [("uncorrect_id"), ([1]), (9999999999)])
def test_negative(employee_fixture, employee_id):
    response = employee_fixture.api_client.employee.delete_employee(employee_id)
    assert response.status_code == 404 or 422, "Статус код не соответствует ожидаемому"