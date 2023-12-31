import sys
import json
import re
from wol_shared import *

name = ""
macaddr = ""
ipaddr = ""
query = ""

x = len(sys.argv)  # not using match fpr python3 < 3.10 compatability
if x == 2:
    macaddr = sys.argv[1].lower()
    query = macaddr
elif x == 3:
    name = sys.argv[1]
    macaddr = sys.argv[2].lower()
    query = name.lower()
elif x == 4:
    name = sys.argv[1]
    macaddr = sys.argv[2].lower()
    ipaddr = sys.argv[3]
    query = name


server_list = get_servers()

query = query.lower()
result_list = []

exactMatch = False
thisQueryTitle = title = (name + " " + macaddr + " " + ipaddr).strip()
for s in server_list.servers:

    if s.macaddr.startswith(query) or s.name.lower().startswith(query):
        title = (s.name + " " + s.macaddr + " " + s.ipaddr).strip()
        if title == thisQueryTitle:
            exactMatch = True
        variables = {"name": s.name, "macaddr": s.macaddr, "ipaddr": s.ipaddr, "uuid": s.uuid}
        match = {"uid": s.uuid, "title": title, "subtitle": s.name, "autocomplete": title, "arg": s.macaddr, "variables": variables}

        result_list.append(match)

if not exactMatch:
    variables = {"name": name, "macaddr": macaddr, "ipaddr": ipaddr}
    valid_mac_addr = bool(re.match('^' + r'[:-]'.join(['([0-9a-f]{2})'] * 6), macaddr))
    thisQuery = {"title": thisQueryTitle, "subtitle": name, "autocomplete": thisQueryTitle, "valid": valid_mac_addr,
                 "arg": macaddr,
                 "variables": variables}
    result_list.append(thisQuery)

result = {"items": result_list}

print(json.dumps(result))
