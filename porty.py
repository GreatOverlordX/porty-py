import socket # for connection
from pyfiglet import Figlet
from colorama import init, Fore


fa = Figlet(font='slant')
print(fa.renderText("Reconnaissance tool"))
fb = Figlet(font="smbraille")
print(fb.renderText("Get to feel\nlike a \n'hacker'"))
fc = Figlet(font="smslant")
print(fc.renderText("Written    by   :\ngOvX   ||   OverlordX"))


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED

def openPort(host, port):
    """
    determine whether `host` has the `port` open
    """
    # Creates a new socket
    s = socket.socket()
    try:
        # attempts to connect to host using that port
        s.connect((host, port))
        # TimeOut if you prefer faster ( less accuracy )
        s.settimeout(0.5) ## 5 milliseconds | comment out/in on preference
    except:
        # CLOSED PORTS/CANNOT CONNECT
        print("Oops! ")
        return False
    else:
        return True

host = input("Enter the host: ")
# Iterate over ports from 1 to 6000 / Change port range if desired!
for port in range(1, 6000):
    if openPort(host, port):
        print(f"  {GREEN}[+] {host}:{port} is open        {RESET}")
    else:
        print(f"  {RED}[!] {host}:{port} is closed       {RESET}", end="\r")
    
