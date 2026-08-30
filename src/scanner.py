import ipaddress
import socket

from mac_vendor_lookup import MacLookup
from scapy.all import ARP, Ether, srp


# Initialize MAC vendor lookup
mac_lookup = MacLookup()


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


def get_vendor(mac_address):
    """Get the manufacturer associated with a MAC address."""
    try:
        return mac_lookup.lookup(mac_address)
    except Exception:
        return "Unknown"


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
        mac = received.hwsrc

        devices.append({
            "ip": received.psrc,
            "mac": mac,
            "vendor": get_vendor(mac)
        })

    return devices


def display_devices(devices):
    """Display discovered network devices."""
    print("=" * 100)
    print("                         NETWORK DEVICE SCANNER")
    print("=" * 100)

    print(
        f"{'IP Address':<20}"
        f"{'MAC Address':<25}"
        f"{'Vendor':<35}"
        f"{'Status':<10}"
    )

    print("-" * 100)

    for device in devices:
        print(
            f"{device['ip']:<20}"
            f"{device['mac']:<25}"
            f"{device['vendor']:<35}"
            f"{'UP':<10}"
        )

    print("-" * 100)
    print(f"Devices Found: {len(devices)}")
    print("=" * 100)


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

    except PermissionError:
        print("\n[!] Permission denied.")
        print("[!] Try running PowerShell as Administrator.")

    except Exception as error:
        print(f"\n[!] Error: {error}")


if __name__ == "__main__":
    main()