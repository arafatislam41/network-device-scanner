import ipaddress
import socket

from mac_vendor_lookup import MacLookup
from scapy.all import ARP, Ether, srp


# Initialize MAC vendor lookup
mac_lookup = MacLookup()

# Common TCP ports
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MSRPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}


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


def scan_ports(target, ports):
    """Scan TCP ports on a target host."""
    results = []

    print(f"\n[+] Scanning TCP ports on: {target}")
    print("[+] Please wait...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((target, port))

            if result == 0:
                results.append({
                    "port": port,
                    "service": COMMON_PORTS.get(port, "Unknown"),
                    "state": "OPEN"
                })

        except socket.error:
            pass

        finally:
            sock.close()

    return results


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


def display_ports(results):
    """Display open TCP ports."""
    print("\n" + "=" * 60)
    print("                       PORT SCAN RESULTS")
    print("=" * 60)

    print(
        f"{'PORT':<12}"
        f"{'STATE':<15}"
        f"{'SERVICE':<20}"
    )

    print("-" * 60)

    if not results:
        print("No open ports found.")

    for result in results:
        print(
            f"{result['port']:<12}"
            f"{result['state']:<15}"
            f"{result['service']:<20}"
        )

    print("-" * 60)
    print(f"Open Ports: {len(results)}")
    print("=" * 60)


def main():
    print("=" * 65)
    print("                 ARAFAT NETWORK SCANNER")
    print("                         VERSION 0.4")
    print("=" * 65)

    try:
        # Detect local network
        local_ip = get_local_ip()
        network = get_network(local_ip)

        print(f"\n[+] Local IP : {local_ip}")
        print(f"[+] Network  : {network}")

        # Discover devices
        devices = scan_network(network)

        display_devices(devices)

        if not devices:
            print("\n[!] No devices discovered.")
            return

        # Ask user for target
        print("\nAvailable targets:")

        for index, device in enumerate(devices, start=1):
            print(
                f"  [{index}] "
                f"{device['ip']} - "
                f"{device['vendor']}"
            )

        choice = input(
            "\nEnter target number for TCP port scan: "
        ).strip()

        if not choice.isdigit():
            print("\n[!] Invalid selection.")
            return

        index = int(choice) - 1

        if index < 0 or index >= len(devices):
            print("\n[!] Target number out of range.")
            return

        target = devices[index]["ip"]

        # Scan common TCP ports
        results = scan_ports(
            target,
            COMMON_PORTS.keys()
        )

        display_ports(results)

    except PermissionError:
        print("\n[!] Permission denied.")
        print("[!] Try running PowerShell as Administrator.")

    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user.")

    except Exception as error:
        print(f"\n[!] Error: {error}")


if __name__ == "__main__":
    main()