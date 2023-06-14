from datetime import datetime

from freezegun import freeze_time

from src.models.message import MQTTMessage


@freeze_time("2023-06-14T10:25:51")
def test_mqtt_message_from_payload() -> None:
    payload = {"humidity/outside": 1.65}
    message = MQTTMessage.from_payload(payload=payload)

    assert message.created_at == datetime.strptime("2023-06-14T10:25:51", '%Y-%m-%dT%H:%M:%S')
    assert message.payload == payload


def test_mqtt_message_dump() -> None:
    payload = {"humidity/outside": 1.65}
    message = MQTTMessage.from_payload(payload=payload)

    message.dump()
