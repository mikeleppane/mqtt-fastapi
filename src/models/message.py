import json
from datetime import datetime
from typing import Any, Self

from loguru import logger
from pydantic import BaseModel


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> str:
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class MQTTMessage(BaseModel):
    created_at: datetime
    payload: Any

    @classmethod
    def from_payload(cls, payload: Any) -> Self:
        """
        Creates MQTTMessage class from the given payload
        :param payload: Any
        :return: MQTTMessage instance
        """
        return cls(created_at=datetime.now().isoformat(), payload=payload)

    def dump(self) -> None:
        """
        Prints the content of the class using pretty formatting
        :return:
        """
        logger.info(json.dumps(self.dict(), sort_keys=True, indent=4, cls=DatetimeEncoder))
