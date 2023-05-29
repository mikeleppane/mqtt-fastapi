import json
from datetime import datetime
from typing import Any, Self

from loguru import logger
from pydantic import BaseModel


class MQTTMessage(BaseModel):
    created_at: str
    payload: Any

    @classmethod
    def from_payload(cls, payload: Any) -> Self:
        """

        :param payload:
        :return: MQTTMessage instance
        """
        return cls(created_at=datetime.now().isoformat(), payload=payload)

    def dump(self) -> None:
        """
        asd
        :return:
        """
        logger.info(json.dumps(self.dict(), sort_keys=True, indent=4))
