import json
from datetime import datetime
from typing import Self, Any

from loguru import logger
from pydantic import BaseModel


class MQTTMessage(BaseModel):
    created_at: str
    payload: Any

    @classmethod
    def from_payload(cls, payload: Any) -> Self:
        return cls(created_at=datetime.now().isoformat(), payload=payload)

    def dump(self):
        logger.info(json.dumps(self.dict(), sort_keys=True, indent=4))
