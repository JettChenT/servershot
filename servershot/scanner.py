from __future__ import annotations
from dataclasses import dataclass

# IP address type
@dataclass
class Addr:
    address: str
    port: None | int = 80

class Scanner:
    name: str
    protocol: str

    def __init__(self, debug=False):
        self.debug = debug
        pass

    def check(self, addr: Addr) -> bool:
        """
        Checks whether the address implements the correct protocol
        :param addr: address to check (including port)
        :return:
        """
        pass

    def scan(self, addr: Addr):
        """
        Scans the address for entry
        :param addr:
        :return:
        """
        pass

    def capture(self):
        pass

    def view(self, url:str):
        pass