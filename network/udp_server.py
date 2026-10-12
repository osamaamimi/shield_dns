import socket

from core.parser import parse
from core.policy_engine import is_blocked
from network.response_builder import build_nxdomin
from network.upstream_resolver import resolve

PORT = 53
HOST = "127.0.0.1"

def handle_request(data):
    domain = parse(data)
    print(f"[+] Parsed domain : {domain}")

    if is_blocked(domain):
        print("[+] policy : BLOCKED")
        return build_nxdomin(data)

    print("[+] policy : ALLOWED")
    return resolve(data)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_server:
        udp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_server.bind((HOST, PORT))
        print(f"[+] DNS server running on port {PORT} ...")

        try:
            while True:
                data, address = udp_server.recvfrom(4096)
                print(f"request from {address}")

                try:
                    response = handle_request(data)
                    udp_server.sendto(response, address)
                except ValueError as e:
                    print(f"[!] bad packet from {address}: {e}")
                except Exception as e:
                    print(f"[!] unexpected error: {e}")

        except KeyboardInterrupt:
            print("[+] server stopped")





