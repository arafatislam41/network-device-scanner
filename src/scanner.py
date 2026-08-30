from scapy.all import ARP, Ether, srp


def scan_network(network):
    print(f"\n[+] Scanning network: {network}")
    print("[+] Please wait...\n")

    # Create ARP request
    arp_request = ARP(pdst=network)

    # Create Ethernet broadcast frame
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Combine Ethernet and ARP packets
    packet = broadcast / arp_request

    # Send packet and receive responses
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
    print("=" * 60)
    print("              NETWORK DEVICE SCANNER")
    print("=" * 60)

    print(f"{'IP Address':<20}{'MAC Address':<25}")
    print("-" * 60)

    for device in devices:
        print(
            f"{device['ip']:<20}"
            f"{device['mac']:<25}"
        )

    print("-" * 60)
    print(f"Devices Found: {len(devices)}")
    print("=" * 60)


def main():
    print("=" * 60)
    print("             ARAFAT NETWORK SCANNER")
    print("=" * 60)

    network = input(
        "\nEnter network range (example: 192.168.1.0/24): "
    )

    devices = scan_network(network)

    display_devices(devices)


if __name__ == "__main__":
    main()