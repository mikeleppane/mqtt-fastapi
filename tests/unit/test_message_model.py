from src.util.deserialize import deserialize


def test_deserialize_should_work_with_valid_payload() -> None:
    payload = b'{"data": 123}'
    payload_deser = deserialize(payload)

    assert type(payload_deser) != bytes
    assert payload_deser == {"data": 123}
