from typing import List, Type, Any
from .scanner import Scanner, Addr
from .scanners import rtsp, rdp
import typer

scans: List[Type[Scanner]] = [rtsp.RtspScanner]
scans_dict = {s.protocol: s for s in scans}

def get_scanner(scanner:str):
    if scanner not in scans_dict:
        # typer raise error
        raise typer.BadParameter(f'Invalid scanner: {scanner}')
    return scans_dict[scanner]()

app = typer.Typer()

@app.command()
def view(url: str, scanner:str):
    scanner = get_scanner(scanner)
    scanner.view(url)

@app.command()
def scan(address: str,port: int, scanner:str):
    scanner = get_scanner(scanner)
    scanner.scan(Addr(address, port))

def main():
    app()

if __name__ == '__main__':
    main()
