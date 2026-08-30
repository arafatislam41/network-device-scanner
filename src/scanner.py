import ipaddress
import socket

from scapy.all import ARP, Ether, srp


def get_local_ip():
    """Get the local IP address of the active network connection."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # No actual connection is made.
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
    finally:
        sock.close()

    return local_ip


def get_network(local_ip, prefix_length=24):
    """Calculate the network CIDR from the local IP."""
    interface = ipaddress.ip_interface(
        f"{local_ip}/{prefix_length}"
    )

    return interface.network


def scan_network(network):
    """Discover active devices using ARP."""
    print(f"\n[+] Scanning network: {network}")
    print("[+] Please wait...\n")

    arp_request = ARP(pdst=str(network))
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    answered, _ = srp(
        packet,
        timeout=3,
        verbose=False
    )

    devices = []

    for _, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def display_devices(devices):
    """Display discovered devices."""
    print("=" * 65)
    print("                 NETWORK DEVICE SCANNER")
    print("=" * 65)

    print(f"{'IP Address':<20}{'MAC Address':<25}{'Status':<10}")
    print("-" * 65)

    for device in devices:
        print(
            f"{device['ip']:<20}"
            f"{device['mac']:<25}"
            f"{'UP':<10}"
        )

    print("-" * 65)
    print(f"Devices Found: {len(devices)}")
    print("=" * 65)


def main():
    print("=" * 65)
    print("                 ARAFAT NETWORK SCANNER")
    print("=" * 65)

    try:
        local_ip = get_local_ip()
        network = get_network(local_ip)

        print(f"\n[+] Local IP : {local_ip}")
        print(f"[+] Network  : {network}")

        devices = scan_network(network)

        display_devices(devices)

    except Exception as error:
        print(f"\n[!] Error: {error}")


if __name__ == "__main__":
    main()