from scapy.all import Packet, PacketList, EDecimal

from datetime import datetime, timezone, timedelta


__all__ = [
    'time',
    'time_between',
    'time_elapsed'
    'time_to_date',
    'time_to_iso',
    'format_duration_readable',
    'format_duration_seconds'
]


#===
def time(pkt: Packet) -> EDecimal:
    """Gets the time associated with a packet.

    Args:
        pkt (Packet): The packet to be queried

    Returns:
        EDecimal: Time of packet
        >>> `1770132796.3301687`
    """
    return pkt.time


def time_between(pkt_a: Packet, pkt_b: Packet) -> EDecimal:
    """Gets the time between two given packets

    Args:
        pkt_a (Packet): Packet A to be queried
        pkt_b (Packet): Packet B to be queried

    Returns:
        EDecimal: Time between the two packets in seconds
        >>> `77.7205855`
    """
    stamp_a = pkt_a.time
    stamp_b = pkt_b.time
    delta_time_between = stamp_b - stamp_a
    return delta_time_between


def time_elapsed(pcap: PacketList) -> EDecimal:
    """Uses `utils.packets.time.time_between` to calculate the total time elapsed of a PCAP

    Args:
        pcap (PacketList): PCAP file to be queried

    Returns:
        EDecimal: Time delta
    """
    first_packet = pcap[0]
    last_packet = pcap[len(pcap) - 1]
    delta_time = time_between(pkt_a=first_packet, pkt_b=last_packet)
    return delta_time


def time_to_date(time: EDecimal) -> datetime:
    """Converts UTC time to readable date time

    Args:
        time (EDecimal): UTC time

    Returns:
        datetime: UTC time converted to a readable date
        >>> `2026-02-03 10:33:16.330169`
    """
    converted_time = float(time) # EDecimal cannot be operated on unless for precise math. Change to float for datetime
    utc_time = datetime.fromtimestamp(converted_time, tz=timezone.utc)
    return utc_time


def time_to_iso(time: EDecimal) -> str: # ISO8601 time standard for logs
    """Formats UTC time to follow ISO8601 timestamp standards

    Args:
        time (EDecimal): time

    Returns:
        str: String-converted time
        >>> `2026-02-03T15:33:16.330169+00:00`
    """
    return datetime.fromtimestamp(
        float(time),
        tz=timezone.utc
    ).isoformat()
    
    
def format_duration_readable(seconds: EDecimal) -> str:
    """Formats EDecimal seconds to DDdHHhMMmSSs

    Args:
        seconds (EDecimal): EDecimal seconds

    Returns:
        str: String formatted timestamp
        >>> `00d00h01m17s`
    """
    td = timedelta(seconds=float(seconds))
    
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400) # total seconds in a day
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f'{days:02d}d{hours:02d}h{minutes:02d}m{seconds:02d}s'


def format_duration_seconds(time: EDecimal, precision: int = None) -> str:
    """Formats EDecimal time to precision-specified seconds

    Args:
        time (EDecimal): time
        precision (int, optional): Precision specification. Defaults to None.

    Returns:
        str: Precision-specified seconds
        >>> `77.721 seconds`
    """
    if precision is None:
        precision = 2
    converted_time = f'{float(time):.{precision}f} seconds'
    return converted_time


if __name__=='__main__':
    print(f'time module LOADED')