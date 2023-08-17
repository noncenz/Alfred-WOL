import pickle
import sys
import json

name = ""
macaddr = ""
ipaddr = ""
query = ""

x = len(sys.argv)  # not using match fpr python3 < 3.10 compatability
if x == 2:
    macaddr = sys.argv[1]
    query = macaddr.lower()
elif x == 3:
    name = sys.argv[1]
    macaddr = sys.argv[2]
    query = name.lower()
elif x == 4:
    name = sys.argv[1]
    macaddr = sys.argv[2]
    ipaddr = sys.argv[3]
    query = name


class Server:
    def __init__(self, name="", ipaddr="", macaddr=""):
        self.name = name
        self.ipaddr = ipaddr
        self.macaddr = macaddr


class ServerList:
    def __init__(self, servers=[]):
        self.servers = servers


with open("servers", "a+b") as f:
    try:
        f.seek(0)
        server_list = pickle.load(f)
    except:
        server_list = ServerList()
    f.close()

query = query.lower()
result_list = []

exactMatch = False
thisQueryTitle = title = (name + " " + macaddr + " " + ipaddr).strip()
for s in server_list.servers:

    if s.macaddr.lower().startswith(query) or s.name.lower().startswith(query):
        title = (s.name + " " + s.macaddr + " " + s.ipaddr).strip()
        if title == thisQueryTitle:
            exactMatch = True
        variables = {"name": s.name, "macaddr": s.macaddr, "ipaddr": s.ipaddr}
        isValid = True
        # mods = {"cmd": {"valid": isValid}}
        match = {"title": title, "subtitle": s.name, "autocomplete": title, "arg": s.macaddr, "variables": variables}

        result_list.append(match)

if not exactMatch:
    variables = {"name": name, "macaddr": macaddr, "ipaddr": ipaddr}
    thisQuery = {"title": thisQueryTitle, "subtitle": name, "autocomplete": thisQueryTitle, "arg": macaddr,
                 "variables": variables}
    result_list.append(thisQuery)

result = {"items": result_list}

print(json.dumps(result))
