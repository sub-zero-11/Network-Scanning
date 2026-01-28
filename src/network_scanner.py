#!/usr/bin/env python3

import socket
import argparse
import threading
import queue
import time
import sys
import pyfiglet
import os

ICE      = "\033[96m"
BLUE     = "\033[94m"
WHITE    = "\033[97m"
GREEN    = "\033[92m"
YELLOW   = "\033[93m"
RED      = "\033[91m"
RESET    = "\033[0m"
BOLD     = "\033[1m"

COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3",
    139: "NETBIOS", 143: "IMAP", 443: "HTTPS",
    445: "SMB", 3306: "MYSQL", 3389: "RDP"
}

def banner():
    os.system("clear")
    art = pyfiglet.figlet_format("NetworkScanning", font="slant")
    print(ICE + art + RESET)
    print(BOLD + BLUE + "❄ Network Enumeration Tool ❄\n" + RESET)

def detect_os(target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target, 80))
        ttl = sock.getsockopt(socket.IPPROTO_IP, socket.IP_TTL)
        sock.close()

        if ttl <= 64:
            return "Linux / Unix"
        elif ttl <= 128:
            return "Windows"
        else:
            return "Unknown"
    except:
        return "Unknown"

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner.split("\n")[0][:60]
    except:
        return "No banner"

def worker():
    while not q.empty():
        port = q.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            if result == 0:
                service = COMMON_SERVICES.get(port, "Unknown")
                banner = grab_banner(target, port)
                print(f"{GREEN}[OPEN]{RESET} {port:<6} {service:<10} | {banner}")
            sock.close()
        except:
            pass
        q.task_done()

parser = argparse.ArgumentParser(description="NetworkScanning Tool")
parser.add_argument("-t", "--target", required=True)
parser.add_argument("-p", "--ports", default="1-1024")
parser.add_argument("--threads", type=int, default=150)
parser.add_argument("--timeout", type=float, default=0.5)
args = parser.parse_args()

target = args.target
timeout = args.timeout
threads = args.threads
start_port, end_port = map(int, args.ports.split("-"))

banner()

q = queue.Queue()
for port in range(start_port, end_port + 1):
    q.put(port)

for _ in range(threads):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()
print("\nScan completed.")
