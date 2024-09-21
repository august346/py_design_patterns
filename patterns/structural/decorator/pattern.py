import base64
import zlib
from abc import ABC, abstractmethod
from functools import wraps
from io import BytesIO
from typing import Callable


def func_to_str(i: int) -> str:
    return str(i)


def bin_decorator(func: Callable[[int], str]) -> Callable[[int], str]:
    @wraps(func)
    def wrapper(i: int) -> str:
        bin_i: int = int("{0:b}".format(i))

        return func(bin_i)

    return wrapper


class DataSource(ABC):
    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(data)

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return "\n".join(file.readlines())


class DataSourceDecorator(DataSource, ABC):
    _source: DataSource

    def __init__(self, source: DataSource):
        self._source = source

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self):
        pass


class EncryptionDecorator(DataSourceDecorator):
    _key: str

    def __init__(self, source: DataSource, key: str):
        super().__init__(source)
        self._key = key

    def write(self, data: str):
        encrypted_data = self._encrypt(data)
        self._source.write(encrypted_data)

    def read(self) -> str:
        encrypted_data = self._source.read()
        return self._decrypt(encrypted_data)

    def _encrypt(self, data: str) -> str:
        return ''.join(chr(ord(c) ^ ord(self._key[i % len(self._key)])) for i, c in enumerate(data))

    def _decrypt(self, data: str) -> str:
        return self._encrypt(data)


class CompressionDecorator(DataSourceDecorator):
    def write(self, data: str):
        compressed_data = self._compress(data)
        self._source.write(compressed_data)

    def read(self) -> str:
        compressed_data = self._source.read()
        return self._decompress(compressed_data)

    @staticmethod
    def _compress(data: str) -> str:
        compressed_bytes = zlib.compress(data.encode())
        return base64.b64encode(compressed_bytes).decode()

    @staticmethod
    def _decompress(data: str) -> str:
        # Decode from base64 and then decompress
        compressed_bytes = base64.b64decode(data.encode())
        return zlib.decompress(compressed_bytes).decode()
