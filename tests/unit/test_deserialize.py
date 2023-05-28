from src.util.deserialize import deserialize


def test_deserialize_should_work_with_valid_payload() -> None:
    payload = b'{"data": 123}'
    payload_deser = deserialize(payload)

    assert type(payload_deser) != bytes
    assert payload_deser == {"data": 123}


def test_deserialize_should_not_work_if_payload_is_not_valid_utf() -> None:
    payload = b'{"data": \xa0\xa1}'
    payload_deser = deserialize(payload)

    assert payload_deser is None


def test_deserialize_should_not_work_if_payload_is_not_valid_json() -> None:
    payload = b'\\'
    payload_deser = deserialize(payload)

    assert payload_deser is None


def test_deserialize_should_work_for_empty_payload() -> None:
    payload = b'{}'
    payload_deser = deserialize(payload)

    assert payload_deser == {}
