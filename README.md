# Passive OT/SCADA Network Monitor

##  Critical Safety Warning
**This tool is designed for PASSIVE monitoring only.**  
It operates in a "listen-only" mode to ensure zero impact on Operational Technology (OT) and Industrial Control Systems (ICS). However, always verify local policies and obtain explicit authorization before connecting any monitoring device to a live SCADA network. Unauthorized monitoring of critical infrastructure may violate federal regulations or company policy.

## Overview
This Python script is a specialized network security tool developed for **Green Energy Solutions**. It allows cybersecurity analysts to monitor traffic in Supervisory Control and Data Acquisition (SCADA) environments without risking operational disruption.

Unlike active scanners (which send probes and can crash legacy PLCs), this tool passively captures and analyzes network packets to identify:
- Active devices communicating over industrial protocols.
- Usage of critical protocols: **Modbus**, **DNP3**, and **BACnet**.
- Anomalalous traffic patterns or unauthorized device communications.

## Features
- **Strictly Passive:** Uses raw socket sniffing without sending any packets (no ARP, no ICMP, no SYN scans).
- **Protocol Detection:** Automatically identifies and flags traffic containing Modbus, DNP3, or BACnet signatures.
- **Device Inventory:** Builds a list of unique IP addresses communicating via industrial protocols.
- **Secure Logging:** Logs findings to a local file with timestamps for audit trails and incident response.
- **Error Handling:** Robust exception handling to prevent script crashes during long-term monitoring.
- **Graceful Shutdown:** Implements signal handlers to ensure logs are saved and resources released on exit.

## Requirements
- **OS:** Linux (Kali, Ubuntu, CentOS) or macOS.
  - *Note: Windows users must install WinPCap/Npcap and may experience limitations with raw sockets.*
- **Python:** Python 3.6+
- **Privileges:** Root/Sudo access is required to bind to network interfaces in promiscuous mode.
- **Dependencies:**
  - `scapy` (Packet manipulation and sniffing)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
