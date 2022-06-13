import fabric
from config_servers import dict_servers
from contextlib import suppress

n = 1
for ip, password in dict_servers.items():
    c = fabric.Connection(ip, port=22, user="root", connect_kwargs={'password': password})

    with suppress(Exception):
        c.run('sudo reboot')

    print(n)
    n += 1