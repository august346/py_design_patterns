import unittest

from . import AuthenticationHandler, AuthorizationHandler, LoggingHandler, ErrorHandler


class TestChainOfResponsibility(unittest.TestCase):

    def setUp(self):
        self.auth_handler = AuthenticationHandler()
        self.authz_handler = AuthorizationHandler()
        self.log_handler = LoggingHandler()
        self.error_handler = ErrorHandler()

        # Setting up the chain: Auth -> Authz -> Log -> Error
        self.auth_handler.set_next(self.authz_handler).set_next(self.log_handler).set_next(self.error_handler)

    def test_authentication(self):
        result = self.auth_handler.handle("authenticate")
        self.assertEqual(result, "User authenticated")

    def test_authorization(self):
        result = self.auth_handler.handle("authorize")
        self.assertEqual(result, "User authorized")

    def test_logging(self):
        result = self.auth_handler.handle("log")
        self.assertEqual(result, "Logging request")

    def test_error_handling(self):
        result = self.auth_handler.handle("error")
        self.assertEqual(result, "Handling error")

    def test_unhandled_request(self):
        result = self.auth_handler.handle("unknown_request")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
