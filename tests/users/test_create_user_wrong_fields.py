# это делаю я
import pytest
@pytest.mark.parametrize("username, age, address, accessed_catalog, exp_code", [
    ([1, 2, 3], 12, "grhgn j", {"name": "idk", "catalog": "phones"}, 422),
    ("Ivan", "five", "ffdhnm", {"name": "blabla", "catalog": "phones"}, 422),
    ("Ivan", 4, ['idk'], {"name": "dgreggggih", "catalog": "phones"}, 422),
    ("Ivan", 5, "dfhurieg", ["idk"], 422)
])

def test_negative(user_fixture, username, age, address, accessed_catalog, exp_code):
    response = user_fixture.api_client.user.create_user(username, age, address, accessed_catalog)

    assert response.status_code == exp_code, "Статус код не соответствует ожидаемому"