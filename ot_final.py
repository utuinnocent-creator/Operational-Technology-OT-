"""
ot_final.py

Passive OT/SCADA Network Traffic Scanner
-----------------------------------------
Green Energy Solutions - OT Security Monitoring

Purpose:
This script passively monitors network traffic on an OT (Operational
Technology) network segment used for SCADA systems in power plant
environments. It listens on a specified network interface and inspects
packets for industrial control protocols (Modbus, DNP3, and BACnet)
without transmitting, injecting, or otherwise interfering with any
traffic on the network. All matching traffic is logged to a local file
(ot_scan_log.txt) for later review by the security team.

Because OT environments are highly sensitive to disruption, this script
uses PyShark's live capture in a purely read-only / listen-only manner
(sniffing only, no packet crafting or sending).
"""

import pyshark


def capture_packets(interface):
    """
    Capture packets passively and handle errors.
    """
    try:
        print(f"Listening on {interface}...")
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=50):
            try:
                filter_ot_traffic(packet)
            except Exception as e:
                print(f"Error processing packet: {e}")
    except Exception as e:
        print(f"Error capturing packets: {e}")


def filter_ot_traffic(packet):
    """
    Filters packets to identify OT-related traffic.
    """
    try:
        if 'MODBUS' in packet or 'DNP3' in packet or 'BACnet' in packet:
            src_ip = packet.ip.src
            dest_ip = packet.ip.dst
            protocol = packet.highest_layer
            log_data(f"OT Traffic Detected: {protocol} from {src_ip} to {dest_ip}")
    except AttributeError:
        pass  # Ignore packets without IP or protocol layers


def log_data(data):
    """
    Logs OT traffic data to a local file for later review.
    """
    try:
        with open("ot_scan_log.txt", "a") as log_file:
            log_file.write(data + "\n")
        print(data)
    except Exception as e:
        print(f"Error logging data: {e}")


def main():
    interface = "eth0"  # Change this based on your network adapter
    print(f"Starting passive scanning on {interface}...")
    capture_packets(interface)


if __name__ == "__main__":
    print("Passive Scanning Script for OT Environment")
    print("Ensure you have the correct network interface configured.")
    print("Logs will be stored in ot_scan_log.txt")
    main()
