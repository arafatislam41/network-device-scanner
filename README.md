# ⚡ Arafat Network Scanner

<p align="center">
  <b>🔎 Local Network Discovery & TCP Port Scanner</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Scapy-2.7.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Network-Scanner-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?style=for-the-badge">
</p>

<p align="center">
  <b>🔎 Discover • 📡 Analyze • 🛡️ Secure</b>
</p>

---

## 🚀 Overview

**Arafat Network Scanner** is a lightweight Python-based network reconnaissance and device discovery tool built with **Scapy**.

The scanner automatically detects the local IPv4 address and network range, discovers active devices using ARP, identifies MAC address vendors, allows the user to select a target, performs TCP port scanning, and generates structured JSON and CSV reports.

This project is designed as a practical learning project combining:

* 🐍 Python
* 🌐 Computer Networking
* 🛡️ Cybersecurity Fundamentals
* 🐧 Linux / Kali Linux Concepts
* 📡 ARP Networking
* 🔌 TCP Networking
* 📊 Network Reporting
* ⚡ Scapy

> ⚠️ **Use this tool only on networks and systems that you own or have explicit permission to test.**

---

## ✨ Features

| Feature                         | Status |
| ------------------------------- | :----: |
| 🔎 Automatic local IP detection |    ✅   |
| 🌐 Automatic network detection  |    ✅   |
| 📡 ARP-based host discovery     |    ✅   |
| 💻 MAC address detection        |    ✅   |
| 🏢 MAC vendor identification    |    ✅   |
| 🟢 Device status detection      |    ✅   |
| 🎯 Interactive target selection |    ✅   |
| 🔌 TCP port scanning            |    ✅   |
| 📋 Basic service identification |    ✅   |
| ⏱️ Discovery & port scan timing |    ✅   |
| 📄 JSON report generation       |    ✅   |
| 📊 CSV report generation        |    ✅   |
| 🌐 HTML report                  |   🔜   |
| 📈 Scan history                 |   🔜   |
| 🖥️ GUI                         |   🔜   |

---

## 🧠 How It Works

```text
                    🌐 LOCAL NETWORK
                           │
                           ▼
                ┌─────────────────────┐
                │  Local IP Detection │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │  Network / CIDR     │
                │    Calculation      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    ARP Discovery    │
                └──────────┬──────────┘
                           │
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
              💻 PC     📱 Phone    📡 IoT
                 │         │         │
                 └─────────┼─────────┘
                           ▼
                ┌─────────────────────┐
                │   MAC Vendor Lookup │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Target Selection  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    TCP Port Scan    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    JSON / CSV       │
                │       Reports       │
                └─────────────────────┘
```

### Discovery

The scanner uses **ARP requests** to identify active devices on the local network.

### Vendor Identification

The MAC address is checked against a vendor database to identify the registered manufacturer.

### Port Scanning

After device discovery, the user can select an authorized target and perform a TCP port scan.

### Reporting

Scan results can be exported to timestamped **JSON** and **CSV** files for further analysis.

---

## 🖥️ Example Output

```text
=================================================================
                 ARAFAT NETWORK SCANNER
                         VERSION 0.5
=================================================================

[+] Local IP : 192.168.0.169
[+] Network  : 192.168.0.0/24

[+] Scanning network: 192.168.0.0/24
[+] Please wait...

====================================================================================================
                         NETWORK DEVICE SCANNER
====================================================================================================
IP Address          MAC Address              Vendor                             Status
----------------------------------------------------------------------------------------------------
192.168.0.1         xx:xx:xx:xx:xx:xx        TP-Link Systems Inc                UP
192.168.0.111       xx:xx:xx:xx:xx:xx        GIGA-BYTE TECHNOLOGY CO.,LTD.      UP
192.168.0.169       xx:xx:xx:xx:xx:xx        ASUSTek COMPUTER INC.              UP
----------------------------------------------------------------------------------------------------
Devices Found: 3
====================================================================================================

[+] Discovery completed in 3.20 seconds.

Available targets:
  [1] 192.168.0.1 - TP-Link Systems Inc
  [2] 192.168.0.111 - GIGA-BYTE TECHNOLOGY CO.,LTD.
  [3] 192.168.0.169 - ASUSTek COMPUTER INC.

Enter target number for TCP port scan: 2

[+] Scanning TCP ports on: 192.168.0.111
[+] Please wait...

============================================================
                       PORT SCAN RESULTS
============================================================
PORT        STATE          SERVICE
------------------------------------------------------------
135         OPEN           MSRPC
------------------------------------------------------------
Target      : 192.168.0.111
Open Ports  : 1
Scan Time   : 6.10 seconds
============================================================
```

> Example IP addresses and MAC addresses are shown for demonstration purposes.

---

## 📊 Reports

The scanner generates timestamped reports inside the `reports/` directory.

### JSON

```text
reports/scan_YYYY-MM-DD_HH-MM-SS.json
```

JSON reports can contain:

* 🌐 Network information
* 💻 Discovered devices
* 📍 IP addresses
* 🔗 MAC addresses
* 🏢 Vendor information
* 🟢 Device status
* ⏱️ Discovery timing

### CSV

```text
reports/scan_YYYY-MM-DD_HH-MM-SS.csv
```

CSV reports are useful for:

* 📊 Spreadsheet analysis
* 📋 Network inventory
* 🔎 Network auditing
* 📈 Future data processing

> Generated local scan reports are excluded from Git tracking to avoid accidentally publishing private network information.

---

## 🛠️ Technology Stack

```text
🐍 Python 3.14+
📡 Scapy 2.7.0
🌐 IPv4 / CIDR
📡 ARP
🔌 TCP
🏷️ MAC OUI / Vendor Lookup
📄 JSON
📊 CSV
🔧 Git / GitHub
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/arafatislam41/network-device-scanner.git
cd network-device-scanner
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

#### Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

#### Linux / Kali Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scanner from the project root:

```bash
python .\src\scanner.py
```

The scanner will automatically detect your local IPv4 address and network.

Example:

```text
[+] Local IP : 192.168.0.169
[+] Network  : 192.168.0.0/24
```

The scanner will then:

1. 🔎 Discover active devices
2. 🏷️ Identify MAC vendors
3. 📋 Display discovered devices
4. 🎯 Ask you to select a target
5. 🔌 Perform TCP port scanning
6. 📄 Generate JSON report
7. 📊 Generate CSV report

---

## 🗂️ Project Structure

```text
network-device-scanner/
│
├── 📁 src/
│   ├── 🐍 scanner.py
│   ├── 🌐 network.py
│   ├── 🔌 ports.py
│   └── 📊 report.py
│
├── 📁 tests/
│
├── 📁 docs/
│
├── 📁 screenshots/
│
├── 📁 reports/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 LICENSE
```

---

## 🧩 Project Modules

### `scanner.py`

Main application responsible for:

* Device discovery
* Vendor lookup
* Target selection
* Port scanning
* Console output
* Scan timing

### `network.py`

Handles:

* Local IP detection
* Local network calculation
* IPv4/CIDR operations

### `ports.py`

Handles:

* TCP port scanning
* Open port detection
* Basic service identification

### `report.py`

Handles:

* JSON report generation
* CSV report generation
* Timestamped report filenames

---

## 🛣️ Roadmap

### Phase 1 — Network Discovery

* [x] Project setup
* [x] Git/GitHub integration
* [x] Automatic local IP detection
* [x] Automatic network detection
* [x] ARP host discovery
* [x] MAC address detection

### Phase 2 — Network Intelligence

* [x] MAC vendor identification
* [x] Device status
* [x] Interactive target selection
* [x] Scan timing

### Phase 3 — Port Analysis

* [x] TCP port scanning
* [x] Open port detection
* [x] Basic service identification

### Phase 4 — Reporting

* [x] JSON export
* [x] CSV export
* [x] Timestamped reports
* [ ] HTML report
* [ ] Scan history

### Phase 5 — Advanced Features

* [ ] ICMP latency detection
* [ ] Custom port ranges
* [ ] Multithreaded scanning
* [ ] Device classification
* [ ] Network topology visualization
* [ ] Professional CLI arguments
* [ ] Configuration file
* [ ] Automated tests
* [ ] Windows executable
* [ ] Linux/Kali optimization

---

## 🎯 Project Goals

This project is being developed as a practical **Networking + Cybersecurity learning project**.

```text
🌐 Understand Network Discovery
📡 Learn ARP Networking
🔌 Understand TCP Services
🐍 Improve Python
🛡️ Practice Security Fundamentals
📊 Learn Network Reporting
🔧 Build Real-World IT Tools
📚 Maintain Professional Documentation
```

---

## 🔐 Responsible Use

This software is intended for:

* ✅ Personal networks
* ✅ Home labs
* ✅ Authorized network administration
* ✅ Cybersecurity education
* ✅ Authorized security testing

**Never scan networks, systems, or devices without appropriate authorization.**

The author is not responsible for unauthorized or improper use of this software.

---

## 👨‍💻 Author

### Md. Arafat Islam

💻 IT & Networking
🌐 Network Engineering
🛡️ Cybersecurity
🐧 Linux / Kali Linux
⚡ Electronics & Hardware

---

<p align="center">

<b>⭐ If you find this project useful, consider giving it a star!</b>

<br><br>

⚡ <b>Discover</b>   •  
📡 <b>Analyze</b>   •  
🛡️ <b>Secure</b>

</p>
