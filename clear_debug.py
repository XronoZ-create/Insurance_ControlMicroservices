import fabric

from config_servers import dict_servers

for ip, password in dict_servers.items():
    c = fabric.Connection(ip, port=22, user="root", connect_kwargs={'password': password})

    result = c.put(local='debug.log', remote='/root/SmallSteamBot/debug.log')
    print(result)