\# 🌐 Network Device Scanner



<p align="center">



<img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge\&logo=python\&logoColor=white">

<img src="https://img.shields.io/badge/Scapy-2.7.0-red?style=for-the-badge">

<img src="https://img.shields.io/badge/Platform-Windows%2011-0078D6?style=for-the-badge\&logo=windows\&logoColor=white">

<img src="https://img.shields.io/badge/Network-Security-8A2BE2?style=for-the-badge">

<img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge">



</p>



<p align="center">

&#x20; <b>🔎 Discover • 📡 Analyze • 🛡️ Secure</b>

</p>



\---



\## 🚀 About



\*\*Network Device Scanner\*\* is a lightweight Python-based networking tool designed to discover active devices on an authorized local network.



The project is built as a practical learning project combining:



\* 🐍 Python

\* 🌐 Computer Networking

\* 🛡️ Cybersecurity Fundamentals

\* 🐧 Linux / Kali Linux Concepts

\* 📡 ARP Networking

\* ⚡ Scapy



> ⚠️ \*\*Use this tool only on networks you own or have explicit permission to test.\*\*



\---



\## ✨ Current Features



| Feature                  | Status |

| ------------------------ | :----: |

| 🔎 Host Discovery        |    ✅   |

| 🌐 IP Address Detection  |    ✅   |

| 💻 MAC Address Detection |    ✅   |

| 📡 ARP-based Discovery   |    ✅   |

| 🏷️ Vendor Detection     |   🔜   |

| ⏱️ Ping / Latency        |   🔜   |

| 🔌 Port Scanning         |   🔜   |

| 📊 Network Reports       |   🔜   |

| 📁 JSON Export           |   🔜   |

| 📑 CSV Export            |   🔜   |

| 🌐 HTML Report           |   🔜   |

| 🖥️ GUI                  |   🔜   |



\---



\## 🧠 How It Works



```text

&#x20;                🌐 LOCAL NETWORK

&#x20;                       │

&#x20;                       ▼

&#x20;               ┌───────────────┐

&#x20;               │ ARP Discovery │

&#x20;               └───────┬───────┘

&#x20;                       │

&#x20;             ┌─────────┼─────────┐

&#x20;             ▼         ▼         ▼

&#x20;          💻 PC      📱 Phone    📡 IoT

&#x20;             │         │         │

&#x20;             └─────────┼─────────┘

&#x20;                       ▼

&#x20;               📋 Device List

```



The scanner sends ARP requests to the specified local network and collects responses from active devices.



\---



\## 🛠️ Technology Stack



```text

🐍 Python

📡 Scapy

🌐 ARP

🪟 Windows 11

🔧 Git / GitHub

```



\---



\## 📦 Installation



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR\_USERNAME/network-device-scanner.git

cd network-device-scanner

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the environment



\*\*Windows PowerShell:\*\*



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



\### 4. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\---



\## ▶️ Usage



Run:



```bash

python .\\src\\scanner.py

```



Enter your authorized local network range when prompted:



```text

Enter network range (example: 192.168.1.0/24):

```



Example:



```text

192.168.1.0/24

```



\---



\## 📊 Example Output



```text

============================================================

&#x20;            ARAFAT NETWORK SCANNER

============================================================



\[+] Scanning network: 192.168.1.0/24

\[+] Please wait...



============================================================

&#x20;             NETWORK DEVICE SCANNER

============================================================



IP Address          MAC Address

\------------------------------------------------------------

192.168.1.1         AA:BB:CC:DD:EE:FF

192.168.1.5         11:22:33:44:55:66

192.168.1.10        77:88:99:AA:BB:CC

\------------------------------------------------------------

Devices Found: 3

============================================================

```



\---



\## 🗂️ Project Structure



```text

network-device-scanner/

│

├── 📁 src/

│   └── 🐍 scanner.py

│

├── 📁 tests/

│

├── 📁 docs/

│

├── 📁 screenshots/

│

├── 📄 README.md

├── 📄 requirements.txt

├── 📄 .gitignore

└── 📄 LICENSE

```



\---



\## 🛣️ Roadmap



\### Phase 1 — Discovery



\* \[x] Project setup

\* \[x] Git repository

\* \[x] ARP device discovery

\* \[x] IP detection

\* \[x] MAC detection



\### Phase 2 — Intelligence



\* \[ ] MAC vendor detection

\* \[ ] Ping latency

\* \[ ] Device classification

\* \[ ] Network interface detection



\### Phase 3 — Security



\* \[ ] Authorized port scanning

\* \[ ] Service identification

\* \[ ] Basic risk indicators

\* \[ ] Network security report



\### Phase 4 — Reporting



\* \[ ] JSON export

\* \[ ] CSV export

\* \[ ] HTML report

\* \[ ] Scan history



\### Phase 5 — Interface



\* \[ ] Professional CLI

\* \[ ] Interactive menu

\* \[ ] GUI

\* \[ ] Windows executable



\---



\## 🎯 Project Goals



This project is being developed as a practical \*\*Networking + Cybersecurity learning project\*\*.



The main goals are:



```text

🌐 Understand Network Discovery

📡 Learn ARP Networking

🐍 Improve Python

🛡️ Practice Security Fundamentals

🔧 Build Real-World IT Tools

📚 Maintain Professional Documentation

```



\---



\## ⚠️ Disclaimer



This software is intended for \*\*educational purposes, network administration, and authorized security testing\*\*.



Do not scan networks, systems, or devices without appropriate authorization.



The author is not responsible for unauthorized or improper use of this software.



\---



\## 👨‍💻 Author



\*\*Md. Arafat Islam\*\*



💻 IT \& Networking

🛡️ Cybersecurity

🐧 Linux / Kali Linux

⚡ Electronics \& Hardware



\---



<p align="center">



<b>⭐ If you find this project useful, consider giving it a star!</b>



<br><br>



🔎 <b>Discover</b>   •  

📡 <b>Analyze</b>   •  

🛡️ <b>Secure</b>



</p>



