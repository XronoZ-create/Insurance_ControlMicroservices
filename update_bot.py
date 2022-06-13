import os
import pysftp
import fabric
from contextlib import suppress
from config_servers import dict_servers

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def put_r_portable(sftp, localdir, remotedir, preserve_mtime=False):
    for entry in os.listdir(localdir):
        remotepath = remotedir + "/" + entry
        localpath = os.path.join(localdir, entry)
        if not os.path.isfile(localpath):
            try:
                sftp.mkdir(remotepath)
            except OSError:
                pass
            put_r_portable(sftp, localpath, remotepath, preserve_mtime)
        else:
            sftp.put(localpath, remotepath, preserve_mtime=preserve_mtime)


for ip, password in dict_servers.items():
    print("Приступил")
    c = fabric.Connection(ip, port=22, user="root", connect_kwargs={'password': password})
    print("Подключился")
    with suppress(Exception):
        c.run('sudo rm -r /root/Insurance_RCA')
        print("Удалил")

    with pysftp.Connection(ip, username='root', password=password, cnopts=cnopts) as sftp:
        sftp.makedirs("/root/Insurance_RCA")
        put_r_portable(sftp, 'C:/Users/Insurance/Insurance_RCA', '/root/Insurance_RCA/', preserve_mtime=False)
        print("Перекинул")