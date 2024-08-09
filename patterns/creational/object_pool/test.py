import asyncio
import unittest
from dataclasses import dataclass

from parameterized import parameterized

from . import ObjectPool


@dataclass
class TWorker:
    pool: ObjectPool

    async def run(self, timeout: float = 1.0):
        obj = await self.pool.acquire()
        await asyncio.sleep(timeout)
        await self.pool.release(obj)


class TestFactory(unittest.IsolatedAsyncioTestCase):
    @parameterized.expand(
        [
            [5, 6, 2.1, False],
            [5, 6, 1.9, True],
            [5, 5, 1.1, False],
            [5, 5, 0.9, True],
            [4, 4, 1.1, False],
            [4, 4, 0.9, True],
            [10, 100, 1.1, False, 0.1],
            [10, 100, 0.9, True, 0.1],
        ]
    )
    async def test(self, size: int, workers_num: int, timeout: float, with_exception: bool, run_timeout=1):
        object_pool = ObjectPool(size)

        async def run():
            async with asyncio.timeout(timeout):
                await asyncio.gather(*[TWorker(object_pool).run(run_timeout) for _ in range(workers_num)])

        if with_exception:
            with self.assertRaises(TimeoutError):
                await run()
        else:
            await run()


if __name__ == '__main__':
    unittest.main()
