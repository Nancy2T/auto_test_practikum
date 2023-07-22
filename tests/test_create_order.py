from tests.utils.sender_stand_request import post_create_order, get_status_order_data


def test_create_and_get_order() -> None:
    """тест на проверку получения кода ответа 200"""
    track_id = post_create_order()
    status_code = get_status_order_data(track_id)
    assert status_code == 200

