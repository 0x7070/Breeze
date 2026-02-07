from scapy.all import Packet, EDecimal
from scapy.layers.inet import TCP, UDP, ICMP

from datetime import datetime, timezone, timedelta

__all__ = [
    'time',
    'time_between',
    'time_to_date',
    'time_to_iso',
    'format_duration_readable'
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
def format_duration_readable(seconds: EDecimal) -> str:
    td = timedelta(seconds=float(seconds))
    
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400) # total seconds in a day
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f'{days}d {hours}h {minutes}m {seconds}s'

def format_duration_seconds(time: EDecimal) -> str:
    converted_time = # float time to format .2f seconds

if __name__=='__main__':
    print(f'time module LOADED')