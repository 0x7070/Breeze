#from packages.utils.general.helpers import hr, hrx
from utils.general.helpers import *
from utils.packets.feature_extraction import subtract
from utils.packets.handling import handle

import pandas as pd
from scapy.all import rdpcap

path = '.\\assets\\pcaps\\ping_dns_test.pcapng'
packets = rdpcap(path)
print(packets[0])
print(packets)

hrx()

