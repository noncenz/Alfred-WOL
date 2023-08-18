import pickle
import os
import uuid
from wol_shared import *

name = os.getenv("name")
macaddr = os.getenv("macaddr")
ipaddr = os.getenv("ipaddr")


def object_exists(server_list, query):
    for server in server_list:
        if server.name == query.name and server.ipaddr == query.ipaddr and server.macaddr == query.macaddr:
            return True
    return False


server_list = get_servers()
s = Server(name=name, macaddr=macaddr, ipaddr=ipaddr, uuid=str(uuid.uuid4()))
if not (object_exists(server_list.servers, s)):
    server_list.servers.append(s)
    save_servers(server_list)

print(macaddr)
