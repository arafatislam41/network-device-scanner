import time

from mac_vendor_lookup import MacLookup
from scapy.all import ARP, Ether, srp

from network import get_local_ip, get_network
from ports import scan_ports
from report import save_json, save_csv


mac_lookup = MacLookup()


def get_vendor(mac_address):
    """Return the manufacturer associated with a MAC address."""
    try:
        return mac_lookup.lookup(mac_address)
    except Exception:
        return "Unknown"


def discover_devices(network):
    """Discover active devices on the local network using ARP."""

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
            "vendor": get_vendor(mac),
            "status": "UP"
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
            f"{device['status']:<10}"
        )

    print("-" * 100)
    print(f"Devices Found: {len(devices)}")
    print("=" * 100)


def choose_target(devices):
    """Allow the user to select a discovered device."""

    if not devices:
        return None

    print("\nAvailable targets:")

    for index, device in enumerate(devices, start=1):
        print(
            f"  [{index}] "
            f"{device['ip']} - "
            f"{device['vendor']}"
        )

    while True:
        try:
            choice = int(
                input("\nEnter target number for TCP port scan: ")
            )

            if 1 <= choice <= len(devices):
                return devices[choice - 1]

            print("[!] Invalid target number.")

        except ValueError:
            print("[!] Please enter a number.")


def display_port_results(target, results, elapsed):
    """Display TCP port scan results."""

    print("\n" + "=" * 60)
    print("                       PORT SCAN RESULTS")
    print("=" * 60)

    print(
        f"{'PORT':<12}"
        f"{'STATE':<15}"
        f"{'SERVICE':<20}"
    )

    print("-" * 60)

    for result in results:
        print(
            f"{result['port']:<12}"
            f"{result['state']:<15}"
            f"{result['service']:<20}"
        )

    print("-" * 60)
    print(f"Target      : {target}")
    print(f"Open Ports  : {len(results)}")
    print(f"Scan Time   : {elapsed:.2f} seconds")
    print("=" * 60)


def main():
    print("=" * 65)
    print("                 ARAFAT NETWORK SCANNER")
    print("                         VERSION 0.6")
    print("=" * 65)

    try:
        local_ip = get_local_ip()
        network = get_network(local_ip)

        print(f"\n[+] Local IP : {local_ip}")
        print(f"[+] Network  : {network}")

        start_time = time.perf_counter()

        devices = discover_devices(network)

        discovery_time = time.perf_counter() - start_time

        display_devices(devices)

        # Save discovered devices to reports
        json_report = save_json(network, devices)
        csv_report = save_csv(devices)

        print(f"\n[+] JSON report: {json_report}")
        print(f"[+] CSV report : {csv_report}")

        print(
            f"\n[+] Discovery completed "
            f"in {discovery_time:.2f} seconds."
        )

        target = choose_target(devices)

        if target is None:
            print("\n[!] No devices found.")
            return

        print(
            f"\n[+] Scanning TCP ports on: "
            f"{target['ip']}"
        )
        print("[+] Please wait...\n")

        port_start = time.perf_counter()

        results = scan_ports(target["ip"])

        port_time = time.perf_counter() - port_start

        display_port_results(
            target["ip"],
            results,
            port_time
        )

    except PermissionError:
        print("\n[!] Permission denied.")
        print("[!] Try running PowerShell as Administrator.")

    except Exception as error:
        print(f"\n[!] Error: {error}")


if __name__ == "__main__":
    main()