## System must have tshark and pyshark installed.

import pyshark, sys, os, platform
from urllib.parse import unquote

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

cap = pyshark.FileCapture(sys.argv[1])

if platform.system() == 'Linux':
    os.system('clear')
elif platform.system() == 'windows':
    os.system('cls')

j = 1
for i in cap:
    try:
        pac1 = i.ip.src_host
        pac2 = i.ip.dst_host
        pac3 = i.http.host
        pac4 = i.http.user_agent
        pac5 = unquote(i.http.request_uri)
        print(color.BLUE + color.BOLD + "\nPacket" + color.END, "[{}]".format(int(j)), '\r')
        print(color.RED + color.BOLD + "ip.src_host: " + color.END, pac1, '\r')
        print(color.RED + color.BOLD + "ip.dst_host: " + color.END, pac2, '\r')
        print(color.RED + color.BOLD + "http.host: " + color.END, pac3, '\r')
        print(color.RED + color.BOLD + "http.user_agent: " + color.END, pac4, '\r')
        print(color.RED + color.BOLD + "http.request_uri: " + color.END, pac5, '\n')
        print('-' * os.get_terminal_size()[0])
    except AttributeError:
        pass
    j+=1