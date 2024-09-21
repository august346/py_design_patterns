import unittest
from typing import Callable

from parameterized import parameterized

from . import RealService, ProxyService, Client


class TestProxyPattern(unittest.TestCase):
    def test_real_service(self):
        service = RealService()
        self.assertEqual(service.request(), "Real service: Handling request")

    @parameterized.expand(
        [
            [ProxyService().request],
            [Client(ProxyService()).make_request]
        ]
    )
    def test_client_with_proxy(self, get_response: Callable[[], str]):
        with self.assertLogs('patterns.structural.proxy.pattern', level='INFO') as log:
            response = get_response()
            self.assertIn("Proxy: Creating the real service object", log.output[0])
            self.assertIn("Proxy: Checking access", log.output[1])
            self.assertIn("Proxy: Logging access to the real service", log.output[2])
            self.assertIn("Proxy: Access granted", response)
            self.assertIn("Real service: Handling request", response)


if __name__ == '__main__':
    unittest.main()
