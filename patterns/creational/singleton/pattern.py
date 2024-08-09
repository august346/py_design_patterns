from typing import Optional


class Singleton:
    _object: Optional["Singleton"] = None

    def __new__(cls, *args, **kwargs):
        if cls._object is None:
            cls._object = super(cls, Singleton).__new__(cls)

        return cls._object
