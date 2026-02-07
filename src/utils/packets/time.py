from scapy.all import Packet, EDecimal
from scapy.layers.inet import TCP, UDP, ICMP

from datetime import datetime, timezone

__all__ = [
    '',
]

def time(pkt: Packet) -> EDecimal:
    return pkt.time

def time_between(pkt_a: Packet, pkt_b: Packet) -> EDecimal:
    stamp_a = pkt_a.time
    stamp_b = pkt_b.time
    delta_time_between = stamp_b - stamp_a
    return delta_time_between

def time_to_date(time: EDecimal) -> datetime:
    converted_time = float(time) # EDecimal cannot be operated on unless for precise math. Change to float for datetime
    utc_time = datetime.fromtimestamp(converted_time)
    return utc_time

def time_to_iso(time: EDecimal): # ISO8601 time standard for logs
    return datetime.fromtimestamp(
        float(time),
        tz=timezone.utc
    ).isoformat()
    
# TODO: Time to seconds, then time to human readable

if __name__=='__main__':
    print(f'time module LOADED')