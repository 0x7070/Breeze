#from packages.utils.general.helpers import hr, hrx
from utils.general.helpers import *

from utils.packets.feature_extraction import count, utc_stamp
from utils.packets.handling import filter_packet, get_packets
from utils.packets.time import time_between, time_to_date, time_to_iso, time, format_duration_readable, format_duration_seconds

import pandas as pd
from scapy.all import rdpcap

path = '.\\src\\assets\\pcaps\\ping_dns_test.pcapng'
packets = rdpcap(path)
print(packets[0])
print(packets)

print(f'Count of PCAP: {count(packets)}')

hrx()

# p0 = packets[0]
# p1 = packets[len(packets) - 1]
# print(f'time of p0: {utc_stamp(p0)}')
# print(f'time of p0: {utc_stamp(p1)}')
# d_p = time_between(p0, p1)
# print(f'delta time: {d_p}')
# print(f'type delta time: {type(d_p)}')
# print(f'Converted time: {format_duration_readable(d_p)}')
# print(f'Formatted time: {format_duration_seconds(time=d_p, precision=3)}')
# date = time_to_date(p0.time)
# print(f'Converted time `{date}`')
# t = time(p0)
# iso = time_to_iso(t)
# print(f'Time: {t}, type: {type(t)}')
# print(f'ISO Time: {iso}, type: {type(iso)}')

packets_for_filtering = rdpcap(path)
p_count = count(packets_for_filtering)

filtered_packets = []
for pkt in packets:
    if filter_packet(
        pkt=pkt,
        ignore_ips=['20.69.136.49'],
        target_ip_fields=['all']
    ):
        filtered_packets.append(pkt)
        
p_count2 = len(filtered_packets)

print(f'pre filter count:  {p_count['Total']}\npost filter count: {p_count2}')

hrx()

packets = get_packets(
    pcap_path=path,
    ignore_ips=['20.69.136.49']
)
print(count(packets))