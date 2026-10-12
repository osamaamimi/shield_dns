import socket
from network.response_builder import build_servfail

UPSTREAM_ADDRESS = "8.8.8.8"
UPSTREAM_PORT = 53
TIMEOUT = 5

def resolve(dns_request_packet):

    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sock :
        sock.settimeout(TIMEOUT)

        try:
            print("[+] DNS request packet sent")
            sock.sendto(dns_request_packet,(UPSTREAM_ADDRESS ,UPSTREAM_PORT))
    
            dns_response_packet,address=sock.recvfrom(4096)
            print(f"[+] response received from {address}")
            return dns_response_packet
        except socket.timeout:
            print("error : timeout !")
            return build_servfail(dns_request_packet)
        except OSError :
            return build_servfail(dns_request_packet)
