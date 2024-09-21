import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ServiceInterface(ABC):
    @abstractmethod
    def request(self) -> str:
        pass


class RealService(ServiceInterface):
    def request(self) -> str:
        return "Real service: Handling request"


class ProxyService(ServiceInterface):
    _real_service: RealService

    def __init__(self, real_service: RealService = None):
        self._real_service = real_service

    def request(self) -> str:
        if self._real_service is None:
            self._real_service = RealService()
            logger.info("Proxy: Creating the real service object")

        if not self._check_access():
            return "Proxy: Access denied"

        self.log_access()
        return f"Proxy: Access granted\n{self._real_service.request()}"

    @staticmethod
    def _check_access() -> bool:
        logger.info("Proxy: Checking access")
        return True

    @staticmethod
    def log_access():
        logger.info("Proxy: Logging access to the real service")


class Client:
    def __init__(self, service: ServiceInterface):
        self._service = service

    def make_request(self) -> str:
        return self._service.request()
