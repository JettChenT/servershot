from ..scanner import Scanner, Addr

class RdpScanner(Scanner):
    name = 'rdp scanner'
    protocol = 'rdp'

    def __init__(self, debug=False):
        super().__init__(debug)

    def check(self, addr: Addr) -> bool:
        return True

    def scan(self, addr: Addr):
        pass

    def capture(self):
        pass

    def view(self, url:str):
        pass