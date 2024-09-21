class CPU:
    @staticmethod
    def freeze():
        print("CPU freezing.")

    @staticmethod
    def jump(position: int):
        print(f"CPU jumping to position {position}.")

    @staticmethod
    def execute():
        print("CPU executing instructions.")


class Memory:
    @staticmethod
    def load(position: int, data: str):
        print(f"Memory loading data '{data}' at position {position}.")


class HardDrive:
    @staticmethod
    def read(lba: int, size: int) -> str:
        print(f"HardDrive reading {size} bytes from LBA {lba}.")
        return "data"


class ComputerFacade:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hard_drive = HardDrive()

    def start(self):
        self._cpu.freeze()
        data = self._hard_drive.read(0, 1024)
        self._memory.load(0, data)
        self._cpu.jump(0)
        self._cpu.execute()
