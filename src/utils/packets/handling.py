from scapy.all import Packet, PacketList, rdpcap
from scapy.layers.inet import IP, TCP, UDP, ICMP

__all__ = [
    'filter_packet',
    'get_packets'
]

#===

# start/end_time?
def filter_packet(pkt: Packet, target_ip_fields: list = None,
                  ignore_ips: list = None, ignore_protocols: list = None, ignore_ports: list = None) -> bool:
    EXCLUDE_PACKET = False
    INCLUDE_PACKET = True
    
    if not pkt:
        err = f'Packet must be passed as type `scapy.Packet`. Got {type(pkt)} instead.'
        raise ValueError(err)
    
    # skip non-ip packets
    if IP not in pkt:
        return EXCLUDE_PACKET
    
    # ---if there are ips to ignore
    if ignore_ips:
        src = pkt[IP].src
        dst = pkt[IP].dst
        
        # if no ip_fields specified, assume 'all' ip_fields to be checked against
        if not target_ip_fields or 'all' in target_ip_fields:
            # if 'all', then check if src/dst in ignore_ips. if, exclude.
            if src in ignore_ips or dst in ignore_ips:
                return EXCLUDE_PACKET
        else: # specific in ip_fields
            if 'src' in target_ip_fields and src in ignore_ips: # if 'src' for match and src_ip in ignore
                return EXCLUDE_PACKET
            if 'dst' in target_ip_fields and dst in ignore_ips: # if 'dst' for match and dst_ip in ignore
                return EXCLUDE_PACKET
            
    # ---if there are protocols to ignore
    if ignore_protocols: 
        matched = False
        if 'TCP' in ignore_protocols and TCP in pkt:
            matched = True
        elif 'UDP' in ignore_protocols and UDP in pkt:
            matched = True
        elif 'ICMP' in ignore_protocols and ICMP in pkt:
            matched = True
            
        # if any of the protocols were matched against ignore list, exclude.
        if matched:
            return EXCLUDE_PACKET

    # ---if there are ports to ignore
    if ignore_ports:
        sport = pkt.sport if hasattr(pkt, 'sport') else None
        dport = pkt.dport if hasattr(pkt, 'dport') else None
        
        if sport not in ignore_ports and dport not in ignore_ports:
            return EXCLUDE_PACKET
        
    # ---if no matches and if nothing to ignore
    return INCLUDE_PACKET


def get_packets(pcap_path: str, target_ip_fields: list = None, 
                ignore_ips: list = None, ignore_protocols: list = None, ignore_ports: list = None) -> PacketList:
    # if file at path is present/right type CHECK?
    
    packets = rdpcap(pcap_path)
    
    filtered_packets = []
    for pkt in packets:
        if filter_packet(
            pkt=pkt,
            target_ip_fields=target_ip_fields,
            ignore_ips=ignore_ips,
            ignore_protocols=ignore_protocols,
            ignore_ports=ignore_ports
        ):
            filtered_packets.append(pkt)

    return PacketList(filtered_packets)

if __name__=='__main__':
    print('handling module LOADED')
  