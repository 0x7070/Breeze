from scapy.all import Packet, PacketList
from scapy.layers.inet import TCP, UDP, ICMP

__all__ = [
    'count',
]

def count(pcap: PacketList = None, fields: list = None) -> dict:
    """
    Short description of the function.

    A more detailed explanation of what the function does, its purpose, and any 
    important behavior or side effects.

    Args:
        param1 (type): Description of the first parameter.
        param2 (type): Description of the second parameter.

    Returns:
        return_type: Description of the return value.
    
    Raises:
        ExceptionType: Description of the conditions under which the exception is raised.

    Example:
        >>> function_name(param1_value, param2_value)
        expected_output
    """
    if pcap is None:
        raise ValueError('PCAP must be provided. Got `None`')
    if not isinstance(pcap, PacketList):
        err_str = f'PCAP must be type PacketList. Got {type(pcap)}'
        raise TypeError(err_str)
    
    counts = {
        'TCP': 0,
        'UDP': 0,
        'ICMP': 0,
        'Other': 0,
        'Total': 0
    }
    
    for pkt in pcap:
        if TCP in pkt:
            counts['TCP'] += 1
        elif UDP in pkt:
            counts['UDP'] += 1
        elif ICMP in pkt:
            counts['ICMP'] += 1
        else:
            counts['Other'] += 1
        counts['Total'] += 1
        
    if not len(pcap) == counts['Total']:
        raise ArithmeticError('dict counts not equal to pcap len.')
    
    return counts

#===Time
def utc_stamp(pkt: Packet) -> float:
    return float(pkt.time)


if __name__=='__main__':
    print(f'feature_extraction module LOADED')