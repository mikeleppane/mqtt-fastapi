import asyncio
from asyncio import Task
from contextlib import suppress
from dataclasses import dataclass, field


@dataclass
class TaskManager:
    tasks: list[Task] = field(default_factory=list)

    def add(self, task: Task) -> None:
        self.tasks.append(task)

    def is_all_running(self) -> bool:
        return not any(t.done() for t in self.tasks)

    async def cancel_all(self) -> None:
        for task in self.tasks:
            with suppress(asyncio.CancelledError):
                task.cancel()
                await task
