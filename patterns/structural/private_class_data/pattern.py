class Data:
    def __init__(self, sensitive_info: str, configuration: dict):
        self._sensitive_info = sensitive_info
        self._configuration = configuration

    def get_sensitive_info(self) -> str:
        return self._sensitive_info

    def get_configuration(self) -> dict:
        return self._configuration.copy()

    def update_configuration(self, key: str, value):
        if key in self._configuration:
            self._configuration[key] = value
        else:
            raise KeyError(f"Key '{key}' not found in configuration.")


class SecureDataWrapper:
    def __init__(self, sensitive_info: str, configuration: dict):
        self._data = Data(sensitive_info, configuration)

    def view_sensitive_info(self) -> str:
        return self._data.get_sensitive_info()

    def view_configuration(self) -> dict:
        return self._data.get_configuration()

    def modify_configuration(self, key: str, value):
        self._data.update_configuration(key, value)
