import asyncio

import pytest

from src.util.task_manager import TaskManager


async def _run_forever() -> None:
    while True:
        await asyncio.sleep(1)


def test_taskman_empty() -> None:
    assert TaskManager().is_all_running()


@pytest.mark.asyncio
async def test_taskman_add_task() -> None:
    # GIVEN
    tm = TaskManager()

    # WHEN
    task = asyncio.create_task(_run_forever())
    tm.add(task)

    # THEN
    assert len(tm.tasks) == 1
    await tm.cancel_all()
    assert tm.is_all_running() is False
