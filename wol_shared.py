import pickle


class Server:
    def __init__(self, name="", ipaddr="", macaddr="", uuid=""):
        self.name = name
        self.ipaddr = ipaddr
        self.macaddr = macaddr
        self.uuid = uuid


class ServerList:
    def __init__(self, servers=[]):
        self.servers = servers


def get_servers():
    with open("servers", "a+b") as f:
        try:
            f.seek(0)
            server_list = pickle.load(f)
        except:
            server_list = ServerList()
        f.close()
    return server_list


def save_servers(server_list):
    with open("servers", "w+b") as f:
        pickle.dump(server_list, f)
        f.close()
