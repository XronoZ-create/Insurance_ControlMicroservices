import fabric
import patchwork.transfers
from config_servers import dict_servers
from contextlib import suppress

n = 1
for ip, password in dict_servers.items():
    c = fabric.Connection(ip, port=22, user="root", connect_kwargs={'password': password})

    with suppress(Exception):
        c.run('sudo add-apt-repository ppa:saiarcot895/chromium-dev -y')

    with suppress(Exception):
        c.run('sudo apt-get update')

    with suppress(Exception):
        c.run('sudo apt install -y chromium-browser')



    print(n)
    n += 1