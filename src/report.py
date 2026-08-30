import csv
import json
from datetime import datetime
from pathlib import Path


REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"


def create_report_directory():
    """Create the reports directory if it does not exist."""
    REPORT_DIR.mkdir(exist_ok=True)


def generate_filename(extension):
    """Generate a timestamp-based report filename."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return REPORT_DIR / f"scan_{timestamp}.{extension}"


def save_json(network, devices):
    """Save scan results as a JSON report."""

    create_report_directory()

    report = {
        "scanner": "Arafat Network Scanner",
        "version": "0.6",
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "network": str(network),
        "devices_found": len(devices),
        "devices": devices
    }

    filename = generate_filename("json")

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            report,
            file,
            indent=4
        )

    return filename


def save_csv(devices):
    """Save discovered devices as a CSV report."""

    create_report_directory()

    filename = generate_filename("csv")

    fieldnames = [
        "ip",
        "mac",
        "vendor",
        "status"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for device in devices:
            writer.writerow(device)

    return filename