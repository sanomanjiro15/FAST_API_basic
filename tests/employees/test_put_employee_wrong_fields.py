import pytest


@pytest.mark.parametrize("id_of_employee, name, role, exp_code", [
    ("12", 1, [1, 2, 3], "admin", 422),
    (6, [23], "Ivan", "student", 422),
    ({"idk"}, 'student', "Ivan", [1, 2, 3], 422),
    ([54], [1, 2, 3], "Ivan", 123, 422)
])
def test_negative(employee_fixture, id_of_employee, name, role, exp_code):
    response = employee_fixture.api_client.employee.update_employee(id_of_employee, name, role)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"