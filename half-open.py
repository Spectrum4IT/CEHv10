"""
        Half-Open scanning (SYN-SCAN)
        Spectrum Development Team
        Written in Python with Scapy module.
"""

from scapy.all import *

dst_ip = "192.168.1.1"   # Destination IP address
dst_port = 80            # Destination port (80:HTTP)

recv_pkt = sr1(IP(dst=dst_ip)/TCP(dport=dst_port,flags="S"))

recv_pkt.show()          # We used show() method to display packet response
