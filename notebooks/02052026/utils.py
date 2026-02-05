from scapy.all import Packet, PacketList
from pandas import DataFrame

def count(pcap: PacketList) -> int:
  return len(pcap)

def utc_stamp(p: Packet):
  return float(p.time) # Return UTC time

### Packet Extraction

def get_ips(pcap: PacketList) -> dict:
  ips = []
  for pkt in pcap:
    if IP not in pkt: # Non-IP packets (VLAN, link layer, etc)
      continue

    pkt_dict = {
        'src_ip': pkt[IP].src,
        'dst_ip': pkt[IP].dst
    }
    ips.append(pkt_dict)

  return ips

# input pcap/ip_dict?
def get_unique_packets(pcap: PacketList, target_feature: str) -> DataFrame:
  if target_feature not in ['src_ip', 'dst_ip']:
    print(f'\n[!] ERROR:\n- `get_unique_packets`:\n-- target_feature: {target_feature} NOT [\'src_ip\', \'dst_ip\']')
    return 0

  ips = get_ips(pcap) # get ips
  df_ips = pd.DataFrame(ips) # convert to df
  unique_ips = df_ips[target_feature].value_counts().to_dict() # store unique ips and freqs in dict
  df_unique_ips = pd.DataFrame.from_dict(unique_ips, orient='index', columns=['freq']) # organize by index and freq
  df_unique_ips.index.name = target_feature # name index (above ips)
  df_unique_ips = df_unique_ips.reset_index() # move `index` to its own column, numerical idx's
  df_unique_ips.index = range(1, len(df_unique_ips) + 1) # idx start 1 not 0

  return df_unique_ips


### Utilities

def hr(char: str = None, size: int = None) -> str:
  if char is None:
    char = '='
  if size is None:
    size = 30
  print(f'{char*size}')

