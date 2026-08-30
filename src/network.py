import ipaddress
import socket


def get_local_ip():
    """Get the local IPv4 address."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    finally:
        sock.close()


def get_network(local_ip, prefix_length=24):
    """Calculate the local network CIDR."""

    interface = ipaddress.ip_interface(
        f"{local_ip}/{prefix_length}"
    )

    return interface.network