import socket


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


def scan_ports(target, ports=None):
    """Scan TCP ports on a target host."""

    if ports is None:
        ports = COMMON_PORTS.keys()

    results = []

    for port in ports:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.5)

        try:
            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:
                results.append({
                    "port": port,
                    "service": COMMON_PORTS.get(
                        port,
                        "Unknown"
                    ),
                    "state": "OPEN"
                })

        except socket.error:
            pass

        finally:
            sock.close()

    return results