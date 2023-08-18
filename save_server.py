import pickle
import os
import uuid

name = os.getenv("name")
macaddr = os.getenv("macaddr")
ipaddr = os.getenv("ipaddr")


class Server:
    def __init__(self, name="", ipaddr="", macaddr="", uuid = ""):
        self.name = name
        self.ipaddr = ipaddr
        self.macaddr = macaddr
        self.uuid = uuid


class ServerList:
    def __init__(self, servers=[]):
        self.servers = servers


def object_exists(server_list, query):
    for server in server_list:
        if server.name == query.name and server.ipaddr == query.ipaddr and server.macaddr == query.macaddr:
            return True
    return False


with open("servers", "a+b") as f:
    try:
        f.seek(0)
        server_list = pickle.load(f)
    except:
        server_list = ServerList()
    finally:
        s = Server(name=name, macaddr=macaddr, ipaddr=ipaddr, uuid=str(uuid.uuid4()))

        if not (object_exists(server_list.servers, s)):
            server_list.servers.append(s)
            f.seek(0)
            f.truncate()
            pickle.dump(server_list, f)
    f.close()

print(macaddr)
