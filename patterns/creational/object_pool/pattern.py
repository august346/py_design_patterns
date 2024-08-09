import asyncio
from typing import Any


class ObjectPool:
    def __init__(self, size: int):
        self._objects_queue = asyncio.Queue(maxsize=size)
        self._objects_to_create_counter = size

    async def acquire(self) -> Any:
        if self._objects_queue.empty():
            if self._objects_to_create_counter > 0:
                self._objects_to_create_counter -= 1
                self._objects_queue.put_nowait(object())

        return await self._objects_queue.get()

    async def release(self, obj: Any):
        self._objects_queue.task_done()
        await self._objects_queue.put(obj)
